import json

from api import create_app


def test_get_success():
    test_app = create_app({'TESTING': True})
    test_req = test_app.test_client()

    test_req.post(
        '/api/v1/entries', content_type='application/json',
        data=json.dumps(
            dict(
                title='Failing Test',
                content='A falling test'
            )
        )
    )

    resp = test_req.get('/api/v1/entries/')

    assert resp.status_code == 200
