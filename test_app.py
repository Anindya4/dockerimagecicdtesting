from app import app

def test_home():
    response=app.test_client().get("/")
    assert response.status_code==200
    
    
def test_page_title():
    response = app.test_client().get("/")
    html = response.data.decode()
    assert "<title>Data Visualization Playground</title>" in html
