import json

from api import create_app


def test_get_success():
    test_app = create_app({'TESTING': True})
    test_req = test_app.test_client()

    new_req = test_req.post(
        '/api/v1/entries', content_type='application/json',
        data=json.dumps(
            dict(
                title='Failing Test',
                content='A falling test'
            )
        )
    )

    ent_id = json.loads(new_req.get_data())['Entry created']['eid']

    resp = test_req.get('/api/v1/entries/{}'.format(ent_id))

    assert resp.status_code == 200
