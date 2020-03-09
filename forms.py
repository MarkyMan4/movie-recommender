from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class MovieOptionsForm(FlaskForm):
    choices = [
        ('action-and-adventure', 'Action & Adventure'), 
        ('animation', 'Animation'), ('anime', 'Anime'), 
        ('biography', 'Biography'), ('children', 'Children'), 
        ('comedy', 'Comedy'), ('crime', 'Crime'), 
        ('cult', 'Cult'), ('documentary', 'Documentary'), 
        ('drama', 'Drama'), ('family', 'Family'), 
        ('fantasy', 'Fantasy'), ('food', 'Food'), 
        ('game-show', 'Game Show'), ('history', 'History'), 
        ('horror', 'Horror'), ('independent', 'Independent'), 
        ('musical', 'Musical'), 
        ('mystery', 'Mystery'), ('reality', 'Reality'), 
        ('romance', 'Romance'), ('science-fiction', 'Science-Fiction'), 
        ('sport', 'Sport'), ('stand-up-and-talk', 'Stand-up & Talk'), 
        ('thriller', 'Thriller'), ('travel', 'Travel'), 
        ('adaptation', 'Adaptation')
    ]

    choices.sort()
    
    genres = SelectField('Genre', choices=choices)
    num_results = IntegerField('Number of Results', validators=[NumberRange(min=1, max=5), DataRequired()])
    submit = SubmitField('Find Movies')
