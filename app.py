from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/landmarks')
def landmarks():
    return render_template('landmarks.html')

@app.route('/festivals')
def festivals():
    return render_template('festivals.html')
                                        
@app.route('/art-crafts')
def art_crafts():
    return render_template('art_crafts.html')

@app.route('/cuisine')
def cuisine():
    return render_template('cuisine.html')

@app.route('/ecommerce')
def ecommerce():
    return render_template('ecommerce.html')

@app.route('/tours-travels')
def tours_travels():
    return render_template('tours_travels.html')

@app.route('/games-quizzes')
def games_quizzes():
    return render_template('games_quizzes.html')

@app.route('/videos')
def videos():
    return render_template('videos.html')

@app.route('/about-us')
def about_us():
    return render_template('about_us.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/collaborate')
def collaborate():
    return render_template('collaborate.html')

@app.route('/cultural-indian')
def cultural_indian():
    return render_template('cultural_indian.html')

@app.route('/article1')
def article1():
    return render_template('article1.html')

@app.route('/article2')
def article2():
    return render_template('article2.html')

@app.route('/article3')
def article3():
    return render_template('article3.html')

@app.route('/folklore')
def folklore():
    return render_template('folklore.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    if query:
        routes = {
            'historical landmarks': 'landmarks',
            'festivals': 'festivals',
            'art & crafts': 'art-crafts',
            'cuisine': 'cuisine',
            'ecommerce': 'ecommerce',
            'community': 'community',
            'login': 'login',
            'register': 'register',
            'tours and travels': 'tours-travels',
            'games & quizzes': 'games-quizzes',
            'videos': 'videos',
            'about the website': 'about-us',
            'contact': 'contact',
            'collaborate': 'collaborate',
            'articles': 'article1', # Placeholder for articles
            'upcoming events': 'events', # Ensure you have an 'events' route or handle accordingly
            'calendar': 'calendar', # Ensure you have a 'calendar' route or handle accordingly
            'donate': 'donate' # Ensure you have a 'donate' route or handle accordingly
        }
        # Normalize query to match routes
        query = query.lower().strip()
        route = routes.get(query)
        if route:
            return redirect(url_for(route))
    return render_template('search_results.html', query=query)

@app.route('/feedback', methods=['POST'])
def feedback():
    feedback_content = request.form['feedback']
    # Process the feedback content
    return redirect(url_for('home'))

@app.route('/subscribe', methods=['POST'])
def subscribe_newsletter():
    email = request.form['email']
    # Process the subscription request
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/events')
def events():
    return render_template('events.html')  # Ensure you have an 'events.html' template or handle accordingly

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')  # Ensure you have a 'calendar.html' template or handle accordingly

@app.route('/donate')
def donate():
    return render_template('donate.html')  # Ensure you have a 'donate.html' template or handle accordingly

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
