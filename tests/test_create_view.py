import json

from api import create_app


def test_create_success():
    test_app = create_app({'TESTING': True})
    test_req = test_app.test_client()

    new_req = test_req.post(
        '/api/v1/entries', content_type='application/json',
        data=json.dumps(
            dict(
                title='Failing Test',
                content='A very interesting test.'
            )
        )
    )

    assert new_req.status_code == 201


def test_create_entry_without_name():
    test_app = create_app({'TESTING': True})
    test_req = test_app.test_client()

    new_req = test_req.post(
        '/api/v1/entries', content_type='application/json',
        data=json.dumps(
            dict(title='Test',
                 content='')
        )
    )

    assert new_req.status_code == 400
