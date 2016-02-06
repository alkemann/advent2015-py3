import re

# 123 -> x means that the signal 123 is provided to wire x.
# x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
# p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
# NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
assignPattern = re.compile("(.+) -> (\w+)")
gatePattern = re.compile("(.+) (AND|OR|LSHIFT|RSHIFT) (.+)")


def is_int(v):
    v = str(v).strip()
    return v=='0' or (v if v.find('..') > -1 else v.lstrip('-+').rstrip('0').rstrip('.')).isdigit()


class Seven:

    def __init__(self, strings):
        self.values = {}
        self.gates = {}
        for s in strings:
            m = assignPattern.findall(s)
            self.gates[m[0][1]] = m[0][0]

    def apply_gate(self, name):
        if name in self.values:
            return self.values[name]
        if name not in self.gates:
            print "ERROR %s not in gates" % name
            exit(-1)

        gate = self.gates[name]
        if is_int(gate):
            self.values[name] = int(gate)
        elif ' ' not in gate:
            if gate in self.gates:
                self.apply_gate(gate)
            self.values[name] = self.values[gate]
        elif "NOT" in gate:
            key = gate[4:]
            if key in self.gates:
                self.apply_gate(key)
            self.values[name] = ~ self.values[key] & 65535
        else:
            #complex gate
            self.apply_complex_gate(name, gate)

        if name not in self.values:
            print "ERROR: Value not found for [%s]" % name
            exit(-1)

        del self.gates[name]
        return self.values[name]

    def apply_complex_gate(self, name, gate):
        m = gatePattern.findall(gate)
        if not m:
            print "ERROR [%s] is not valid gate"
            exit(-1)

        left = m[0][0]
        right = m[0][2]

        if is_int(left):
            left = int(left)
        else:
            left = self.apply_gate(left)
        if is_int(right):
            right = int(right)
        else:
            right = self.apply_gate(right)

        value = None
        if m[0][1] == "AND":
            value = left & right
        elif m[0][1] == "OR":
            value = left | right
        elif m[0][1] == "LSHIFT":
            value = left << right
        elif m[0][1] == "RSHIFT":
            value = left >> right
        else:
            print "ERROR wtf are u here for!"
            exit(-1)
        self.values[name] = value

    def check(self, output_name):

        if output_name in self.gates:
            self.apply_gate(output_name)

        if output_name in self.values:
            return self.values[output_name]

        return None
