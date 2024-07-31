from data_visualization import app


def test_title_exists(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#app-title", timeout=10)


def test_graph_exists(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#graph-content", timeout=10)


def test_radio_btns_exists(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#controls-and-radio-item", timeout=10)