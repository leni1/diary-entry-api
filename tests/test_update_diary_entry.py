import json

from api import create_app


def test_update_title_success():
    test_app = create_app({'TESTING': True})
    test_req = test_app.test_client()

    new_req = test_req.post(
        '/api/v1/entries', content_type='application/json',
        data=json.dumps(
            dict(
                title='Failing test',
                content='An interesting test.'
            )
        )
    )

    ent_id = json.loads(new_req.get_data())['Entry created']['eid']

    resp = test_req.put(
        '/api/v1/entries/{}'.format(ent_id),
        content_type='application/json',
        data=json.dumps(
            dict(title='New Title',
                 content='New content.')
        )
    )

    assert resp.status_code == 201


def test_update_content_success():
    test_app = create_app({'TESTING': True})
    test_req = test_app.test_client()

    new_req = test_req.post(
        '/api/v1/entries', content_type='application/json',
        data=json.dumps(
            dict(
                title='Failing test',
                content='An interesting test.'
            )
        )
    )

    ent_id = json.loads(new_req.get_data())['Entry created']['eid']

    resp = test_req.put(
        '/api/v1/entries/{}'.format(ent_id),
        content_type='application/json',
        data=json.dumps(
            dict(
                title='New title',
                content='Some interesting content here.')
        )
    )

    assert resp.status_code == 201
