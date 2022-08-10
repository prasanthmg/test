def test_1(config_env, user_id):
    if config_env == 'dev' and user_id=='me':
        assert 1
    else:
        assert 0
