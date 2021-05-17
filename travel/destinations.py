from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Destination, Comment
from .forms import DestinationForm, CommentForm

bp = Blueprint('destination', __name__, url_prefix='/destinations')

@bp.route('/<id>')
def show(id):
    destination = get_destination()
    commentForm = CommentForm()
    return render_template('destinations/show.html', destination=destination, form=commentForm)

@bp.route('/create', methods=['GET', 'POST']) 
@login_required
def create():
    comment = Comment(text=form.text.data,
    destination=destination_obj, user=current_user)
    print("Method type: ", request.method)
    form = DestinationForm()

    if form.validate_on_submit():
        print("Form successfully submitted")
        return redirect(url_for('destination.create'))

    return render_template('destinations/create.html', form=form)


##############   USE THIS CODE LATER ######################
def get_destination():
    #   creating the description of Brazil
    b_desc= """Brazil is considered an advanced emerging economy.
    It has the ninth largest GDP in the world by nominal, and eight by PPP measures. 
    It is one of the world\'s major breadbaskets, being the largest producer of coffee for the last 150 years."""

    #   an image location
    image_loc='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFyC8pBJI2AAHLpAVih41_yWx2xxLleTtdshAdk1HOZQd9ZM8-Ag'
    destination = Destination('Brazil',b_desc,image_loc,'10 R$')

    #   a comment
    comment = Comment("User1", "Visited during the olympics, was great",'2019-11-12 11:00:00')
    destination.set_comments(comment)

    return destination
