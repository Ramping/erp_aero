from pdf_processing import read_pdf
from itertools import zip_longest
import pytest
from pytest_check import check


@pytest.mark.parametrize("reference_file, checked_file", [("test_task.pdf", 'test_task.pdf')])
def test_check_pdf(reference_file, checked_file):
    reference_file = read_pdf(reference_file)
    verifiable_file = read_pdf(checked_file)
    with check:
        assert verifiable_file.keys() == reference_file.keys(), 'presence of elements does not match'
    for i, k in zip_longest(reference_file, verifiable_file):
        with check:
            assert i == k, 'file structure does not match'
