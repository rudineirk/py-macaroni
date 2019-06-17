import macaroni as mci


class Calculator(mci.Macaroni):
    def increment(self, data):
        print("increment")
        return data + 1

    def decrement(self, data):
        print("decrement")
        return data - 1

    def div_zero(self, data):
        return data / 0

    def power(self, data):
        print("power")
        return data ** 2

    @mci.exception(ZeroDivisionError)
    def handle_zero(self, exc, data):
        print("## zero error")
        return mci.Error("teste")


calc = Calculator(2)
value = (
    calc.increment()
    .increment()
    .div_zero()
    .handle_zero()
    .decrement()
    .power()
    .unwrap()
)

if calc.error:
    print("error", value)
else:
    print("value", value)

calc = Calculator(magic=False)
assert calc.increment(2) == 3
