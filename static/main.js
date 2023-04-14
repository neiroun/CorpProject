window.onload = () => {
    document.getElementById('news_button').onclick = () => {
        document.location = 'news';
    }
    document.getElementById('main_button').onclick = () => {
        document.location = '/';
    }
    document.getElementById('about_button').onclick = () => {
        document.location = 'about';
    }
}