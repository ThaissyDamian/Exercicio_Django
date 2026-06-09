def test_home_page(client):
    response = client.get("/home/")

    assert response.status_code == 200
    assert response.content == b"Hello World"