import pytest

from dual_stack import DualStack

def test_default_size():
    stack = DualStack()
    assert stack.size() == 10

def test_parameterized_size():
    size = 5
    stack = DualStack(size)
    assert stack.size() == 5

def test_zero_size():
    size = -1
    with pytest.raises(ValueError, match=r"size must be positive"):
        stack = DualStack(size)

def test_negative_size():
    size = -1
    with pytest.raises(ValueError, match=r"size must be positive"):
        stack = DualStack(size)

def test_stack1_is_empty():
    stack = DualStack()
    assert stack.stack1_is_empty() == True

def test_stack2_is_empty():
    stack = DualStack()
    assert stack.stack2_is_empty() == True

def test_stack1_push():
    stack = DualStack(5)
    top = stack.stack1_push(10)
    assert top == 0

def test_stack2_push():
    stack = DualStack(5)
    top = stack.stack2_push(20)
    assert top == 4

def test_stack1_overflow():
    stack = DualStack(3)
    stack.stack1_push(0)
    stack.stack1_push(2)
    stack.stack1_push(1)
    with pytest.raises(RuntimeError, match="stack overflow"):
        top = stack.stack1_push(5)

def test_stack2_overflow():
    stack = DualStack(3)
    stack.stack2_push(0)
    stack.stack2_push(2)
    stack.stack2_push(1)
    with pytest.raises(RuntimeError, match="stack overflow"):
        top = stack.stack2_push(5)

def test_stack1_pop():
    stack = DualStack(3)
    stack.stack1_push(0)
    stack.stack1_push(2)
    stack.stack1_push(1)
    assert stack.stack1_pop() == 1
    assert stack.stack1_pop() == 2
    assert stack.stack1_pop() == 0

def test_stack2_pop():
    stack = DualStack(3)
    stack.stack2_push(0)
    stack.stack2_push(2)
    stack.stack2_push(1)
    assert stack.stack2_pop() == 1
    assert stack.stack2_pop() == 2
    assert stack.stack2_pop() == 0

def test_stack1_underflow():
    stack = DualStack(3)
    with pytest.raises(RuntimeError, match="stack underflow"):
        x = stack.stack1_pop()

def test_stack2_underflow():
    stack = DualStack(3)
    with pytest.raises(RuntimeError, match="stack underflow"):
        x = stack.stack2_pop()

def test_stack1_overflow_pop_and_push():
    stack = DualStack(3)
    stack.stack1_push(0)
    stack.stack1_push(2)
    stack.stack1_push(1)
    with pytest.raises(RuntimeError, match="stack overflow"):
        top = stack.stack1_push(5)
    assert stack.stack1_pop() == 1 
    assert stack.stack1_push(3) == 2
    
def test_stack2_overflow_pop_and_push():
    stack = DualStack(3)
    stack.stack2_push(0)
    stack.stack2_push(2)
    stack.stack2_push(1)
    with pytest.raises(RuntimeError, match="stack overflow"):
        top = stack.stack2_push(5)
    assert stack.stack2_pop() == 1 
    assert stack.stack2_push(3) == 0

def test_stack1_and_stack2_combined():
    stack = DualStack(3)
    stack.stack1_push(12)
    stack.stack1_push(1)
    stack.stack2_push(42)
    with pytest.raises(RuntimeError, match="stack overflow"):
        stack.stack1_push(23)
    with pytest.raises(RuntimeError, match="stack overflow"):
        stack.stack2_push(23)
    assert stack.stack1_pop() == 1
    stack.stack2_push(32)
    assert stack.stack1_pop() == 12
    with pytest.raises(RuntimeError, match="stack underflow"):
        stack.stack1_pop()
    assert stack.stack2_pop() == 32
    assert stack.stack2_pop() == 42
    with pytest.raises(RuntimeError, match="stack underflow"):
        stack.stack2_pop()

