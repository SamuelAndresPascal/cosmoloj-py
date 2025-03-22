from pathlib import Path


def test_toto():

    with open(Path(__file__).parent / 'multipleRecords.ris') as s:
        while line := s.readline():
            print(line)
            print(line.endswith("\n"))