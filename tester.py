from SLLQueue import SLLQueue
from SLLStack import SLLStack
from DLList import DLList
from DLLDeque import DLLDeque
from MaxQueue import MaxQueue
import random
from ChainedHashTable import ChainedHashTable

def test():
    """write your own tester in this function"""
    print("Testing MaxQueue...")
    mq = MaxQueue()
    import random

    for i in range(6):
        value = random.randint(1, 20)
        mq.add(value)
        print("Added value:", value)
        print(f"Max Queue: {mq}")
        print(f"Max value: {mq.max()}\n")

    while mq.size() > 0:
        r = mq.remove()
        print(f"Removed:", r)
        print(f"MaxQueue:", mq)
        if mq.size() > 0:
            print(f"Max value: {mq.max()}\n")

    def test_add():
        cht = ChainedHashTable()
        assert cht.add(1, 'A') == True
        assert cht.add(2, 'B') == True
        assert cht.add(1, 'C') == False  # Duplicate key
        assert cht.size() == 2
        print("test_add passed")

    test_add()

    def test_find():
        cht = ChainedHashTable()
        cht.add(1, 'A')
        cht.add(2, 'B')
        assert cht.find(1) == 'A'
        assert cht.find(2) == 'B'
        assert cht.find(3) == None  # Non-existent key
        print("test_find passed")

    test_find()

    def test_remove():
        cht = ChainedHashTable()
        cht.add(1, 'A')
        cht.add(2, 'B')
        print(f"Before removal: {cht}, Size: {cht.size()}")  # Debugging statement
        assert cht.remove(1) == 'A'
        assert cht.remove(3) is None  # Non-existent key
        print(f"After removal: {cht}, Size: {cht.size()}")  # Debugging statement
        assert cht.size() == 1
        print("test_remove passed")

    test_remove()

    def test_resize():
        cht = ChainedHashTable()
        for ele in range(16):
            cht.add(ele, chr(65 + ele))  # Adding 16 elements
        cht.add(17, chr(65 + 17))
        assert cht.size() == 17
        assert len(cht.t) == 32  # Table should resize to 32 bins
        print(len(cht.t))
        print("test_resize passed")

    test_resize()

    def test_collisions():
        cht = ChainedHashTable()
        keys = [1, 17, 33]  # These keys should hash to the same bin if table size is 16
        for key in keys:
            cht.add(key, chr(65 + key))
        assert cht.find(1) == 'B'
        assert cht.find(17) == 'R'
        assert cht.find(33) == 'b'
        print("test_collisions passed")

    test_collisions()

test()