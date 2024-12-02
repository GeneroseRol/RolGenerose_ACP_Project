import pytest
import random

@pytest.fixture
def setup_names():
    allNames = ['Gen', 'Eldon', 'Paquera']
    availableNames = allNames[:]
    pickHistory = []
    return allNames, availableNames, pickHistory

def test_add_names(setup_names):
    allNames, availableNames, pickHistory = setup_names

    allNames.append('John')
    availableNames.append('John')
    assert 'John' in allNames
    assert 'John' in availableNames

def test_pick_random(setup_names):
    allNames, availableNames, pickHistory = setup_names

    picked_name = random.choice(availableNames)
    availableNames.remove(picked_name)
    pickHistory.append(picked_name)

    assert picked_name not in availableNames
    assert picked_name in pickHistory

def test_pick_multiple(setup_names):
    allNames, availableNames, pickHistory = setup_names

    num_to_pick = 2
    picked_names = random.sample(availableNames, num_to_pick)
    for picked in picked_names:
        availableNames.remove(picked)
    pickHistory.extend(picked_names)

    assert len(picked_names) == num_to_pick
    for name in picked_names:
        assert name not in availableNames
    for name in picked_names:
        assert name in pickHistory

def test_reset_names(setup_names):
    allNames, availableNames, pickHistory = setup_names

    availableNames[:] = allNames
    pickHistory.clear()

    assert len(availableNames) == len(allNames)
    assert len(pickHistory) == 0

def test_clear_data(setup_names):
    allNames, availableNames, pickHistory = setup_names

    allNames.clear()
    availableNames.clear()
    pickHistory.clear()

    assert len(allNames) == 0
    assert len(availableNames) == 0
    assert len(pickHistory) == 0

if __name__ == "__main__":
    pytest.main()
