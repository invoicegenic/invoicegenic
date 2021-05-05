'''
'''


def shared_setting(env_vars: dict) -> dict:
    return dict(
        SECRET_KEY=env_vars['SECRET_KEY']
    )
