from app.main import bp


# Test Blueprint (delete after tests)
@bp.route('main/')
def main_bp():
    return 'Main Blueprints works:)'
