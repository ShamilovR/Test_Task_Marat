from pages.log_in import CatalogPage, SearchAuto, ListNodes


def test_login(authorized_driver):
    select = CatalogPage(authorized_driver)
    select.overlay_menu()
    select.open_original_catalog()
    check_search = SearchAuto(authorized_driver)
    check_search.search_by_vin('WAUBH54B11N111054')
    assert ListNodes(authorized_driver).get_header_text() == "Выберите категорию или узел"

