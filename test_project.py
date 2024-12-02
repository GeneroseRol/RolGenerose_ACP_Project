import pytest
import random

@pytest.fixture
def setup_names():
    all_names = ['Gen', 'Eldon', 'Paquera']
    available_names = all_names[:]
    pick_history = []
    return all_names, available_names, pick_history

def test_add_names(setup_names):
    all_names, available_names, pick_history = setup_names

    all_names.append('John')
    available_names.append('John')
    assert 'John' in all_names
    assert 'John' in available_names

def test_pick_random(setup_names):
    all_names, available_names, pick_history = setup_names

    picked_name = random.choice(available_names)
    available_names.remove(picked_name)
    pick_history.append(picked_name)

    assert picked_name not in available_names
    assert picked_name in pick_history

def test_pick_multiple(setup_names):
    all_names, available_names, pick_history = setup_names

    num_to_pick = 2
    picked_names = random.sample(available_names, num_to_pick)
    for picked in picked_names:
        available_names.remove(picked)
    pick_history.extend(picked_names)

    assert len(picked_names) == num_to_pick
    for name in picked_names:
        assert name not in available_names
    for name in picked_names:
        assert name in pick_history

def test_reset_names(setup_names):
    all_names, available_names, pick_history = setup_names

    available_names[:] = all_names
    pick_history.clear()

    assert len(available_names) == len(all_names)
    assert len(pick_history) == 0

def test_clear_data(setup_names):
    all_names, available_names, pick_history = setup_names

    all_names.clear()
    available_names.clear()
    pick_history.clear()

    assert len(all_names) == 0
    assert len(available_names) == 0
    assert len(pick_history) == 0

if __name__ == "__main__":
    pytest.main()
