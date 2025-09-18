class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def hello(self):
        print("Hello from B")
        super().hello()

class C(A):
    def hello(self):
        print("Hello from C")
        super().hello()

class D(B, C):
    def hello(self):
        print("Hello from D")

class E(C):
    pass

class F(B, E):
    pass

print("Task 2")
print(F.mro())

print("Task 3")
try:
    class Base1: pass
    class Base2: pass
    class Child1(Base1, Base2): pass
    class Child2(Base2, Base1): pass
    class GrandChild(Child1, Child2): pass

except TypeError as e:
    print(f"Error: {e}")