from flask import render_template, request, url_for, flash, redirect, current_app
from flask_login import login_required, current_user
from app import db
from app.models.cms.home_editor import HomeEditor
from . import cms

@login_required
@cms.route('/choose-option', methods=['GET', 'POST'])
def cms_about_me():
    return render_template('cms/homedit.html')

@login_required
@cms.route('/edit-description', methods=['GET', 'POST'])
def description_about_me():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']  # Sformatowany HTML z TinyMCE

        # Zakładamy, że pracujesz na rekordzie HomeEditor o id=1
        home_editor = HomeEditor.query.get(1)
        home_editor.title = title
        home_editor.description = description

        db.session.commit()  # Zapisanie zmian do bazy danych

        return redirect(url_for('cms.cms_about_me'))

        # Jeśli metoda GET, wyświetl formularz edytora
    home_editor = HomeEditor.query.get(1)
    return render_template('cms/change_homepage.html', home_editor=home_editor)


@login_required
@cms.route('/change_photo', methods=['GET', 'POST'])
def change_photo():
    # logic xD
    if request.method == 'POST':
        file = request.files['photo']
        if file:
            flash('Photo changed successfully!')
            return redirect(url_for('cms.change_photo'))

    return render_template('cms/change_photo.html')