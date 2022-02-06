from pages.log_in import SelectingTheOriginalDirectory
from pages.log_in import SearchAuto
from pages.log_in import OutputComparison


def test_login(authorized_driver):
    select = SelectingTheOriginalDirectory(authorized_driver)
    select.overlay_menu()
    select.open_original_catalog()
    check_search = SearchAuto(authorized_driver)
    check_search.search_by_vin('WAUBH54B11N111054')
    assert OutputComparison(authorized_driver).get_header_text() == "Выберите категорию или узел"

