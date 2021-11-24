from unittest.mock import patch
from PY_lesson_5_task_2_for_ADPY import documents, directories, delete_doc, add_doc, get_shelf, get_name


def count(collection: dict):
    count = 0
    for item in collection:
        count += len(collection[item])
    return count


class Test_PY_lesson_5_for_ADPY:

    @patch('builtins.input', side_effect=['10006'])  # side_effect эмулирует количество input
    def test_get_name(self, a):
        assert get_name() == 'Аристарх Павлов'

    @patch('builtins.input', side_effect=['1000'])  # side_effect эмулирует количество input
    def test_get_name_wrong_doc(self, a):
        assert get_name() == None

    @patch('builtins.input', side_effect=['10006'])  # side_effect эмулирует количество input
    def test_get_shelf(self, a):
        assert get_shelf() == '2'

    @patch('builtins.input', side_effect=['1000'])  # side_effect эмулирует количество input
    def test_get_shelf_wrong_doc(self, a):
        assert get_shelf() == None

    @patch('builtins.input', side_effect=['1000', 'passport', 'IGOR', '3'])  # side_effect эмулирует количество input
    def test_add_doc_right_input(self, a):
        start_count_doc = len(documents)
        start_count_dir = count(directories)
        add_doc()
        assert start_count_doc + 1 == len(documents) and start_count_dir + 1 == count(directories)

    @patch('builtins.input', side_effect=['1000', 'passport', 'IGOR', '4'])  # side_effect эмулирует количество input
    def test_add_doc_wrong_shelf(self, a):
        start_count_doc = len(documents)
        start_count_dir = count(directories)
        add_doc()
        assert start_count_doc == len(documents) and start_count_dir == count(directories)

    @patch('builtins.input', side_effect=['10006']) # side_effect эмулирует количество input
    def test_delete_doc_right_document(self, a):
        start_count_doc = len(documents)
        start_count_dir = count(directories)
        delete_doc()
        assert start_count_doc == len(documents) + 1 and start_count_dir == count(directories) + 1

    @patch('builtins.input', side_effect=['10007'])  # side_effect эмулирует количество input
    def test_delete_doc_wrong_document(self, a):
        start_count_doc = len(documents)
        start_count_dir = count(directories)
        delete_doc()
        assert start_count_doc == len(documents) and start_count_dir == count(directories)


