"""testing the donation controller"""

import pytest
from Donor import Donor
from DonationController import DonationController


@pytest.fixture
def stw():
    """sample controller for save the whales foundation
    setup with basic information and no donations"""
    return DonationController(name='Save The Whales')


@pytest.fixture
def donor1():
    return Donor(id=1, firstname='Fisher', lastname='Price')


@pytest.fixture
def donor2():
    return Donor(id=2, firstname='Wonky', lastname='Donkey')


def test_create_new_donor(stw, donor1):
    """given a donation controller
    when user creates new donor
    the user is added to the donation controller"""
    assert stw.find_donor(donor1) is None
    stw.create_donor(donor1)
    assert stw.find_donor(donor1) == donor1


def test_create_new_donor_creates_error_if_exists(stw, donor1):
    stw.create_donor(donor1)
    assert stw.find_donor(donor1) == donor1

    with pytest.raises(KeyError):
        stw.create_donor(donor1)

def test_create_donation_for_donor(stw, donor1):
    """given a controller and donor
    when a donation is added to donor
    the controller's total is updated"""
    assert stw.get_total_donations() == 0
    stw.create_donor(donor1)
    stw.create_donation(donor=donor1, amount=500)
    assert stw.get_total_donations() == 500


def test_error_when_create_donation_for_missing_donor(stw, donor1):
    """give user tries to add donation for non-existanant donor
    when the amount is applied
    an exception is returned"""
    with pytest.raises(IndexError):
        stw.create_donation(donor=donor1, amount=500)


def test_send_letters_to_all_donors(stw, donor1, donor2, tmpdir):
    """given controller
    when triggers send letters to donors
    letters are sent to all donors as indicated by letters being generated"""
    # ensure no letters are avaliable
    assert len(tmpdir.listdir())==0

    # create donors
    stw.create_donor(donor1)
    stw.create_donation(donor=donor1, amount=500)
    stw.create_donor(donor2)
    stw.create_donation(donor=donor2, amount=5)

    # verify we have donors otherwise last assert will fail
    stw.send_letters_to_everyone(thank_you_directory=tmpdir)
    assert len(tmpdir.listdir()) > 0

def test_next_id_property(stw, donor1, donor2):
        """tests next id show correct details
        given a blank donor collection
        when next_id called
        1 is returned"""
        assert stw.next_id == 1

        """given a blank donor collection
        when two donors are added and next_id called
        integer above max is returned"""
        stw.create_donor(donor2)
        assert stw.next_id == 1

        stw.create_donor(donor1)
        assert stw.next_id == 3

