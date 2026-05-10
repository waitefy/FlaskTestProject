from flask import Flask, render_template_string


app = Flask(__name__)


@app.route("/")
def index():
    gallery = [
        {
            "title": "Mountain Sunrise",
            "description": "A calm morning view with layered hills and warm colors.",
            "image": "media/mountain.svg",
        },
        {
            "title": "Ocean Wave",
            "description": "A simple blue seascape for a fresh, bright landing page.",
            "image": "media/ocean.svg",
        },
        {
            "title": "City Night",
            "description": "A small skyline illustration with a late-evening mood.",
            "image": "media/city.svg",
        },
    ]

    return render_template_string(
        """
<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Flask Media Gallery</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            font-family: Arial, sans-serif;
            color: #172033;
            background: linear-gradient(135deg, #f7efe5 0%, #eaf4ff 52%, #f4f1ff 100%);
            overflow-x: hidden;
        }

        .page {
            width: min(1120px, calc(100% - 32px));
            margin: 0 auto;
            padding: 48px 0;
        }

        .hero {
            display: grid;
            grid-template-columns: 1.1fr 0.9fr;
            gap: 32px;
            align-items: center;
            padding: 36px;
            border: 1px solid rgba(23, 32, 51, 0.12);
            border-radius: 28px;
            background: rgba(255, 255, 255, 0.72);
            box-shadow: 0 24px 80px rgba(42, 53, 77, 0.14);
            backdrop-filter: blur(12px);
        }

        .eyebrow {
            margin: 0 0 12px;
            color: #5d43d6;
            font-size: 14px;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
        }

        h1 {
            margin: 0;
            font-size: clamp(38px, 8vw, 76px);
            line-height: 0.95;
            letter-spacing: -0.06em;
        }

        .lead {
            max-width: 620px;
            margin: 22px 0 0;
            color: #4a556c;
            font-size: 18px;
            line-height: 1.7;
        }

        .hero-card {
            padding: 16px;
            border-radius: 24px;
            background: #172033;
            color: white;
            transform: rotate(2deg);
        }

        .hero-card img {
            display: block;
            width: 100%;
            border-radius: 18px;
        }

        .hero-card p {
            margin: 14px 6px 4px;
            font-weight: 700;
        }

        .gallery {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin-top: 28px;
        }

        .item {
            overflow: hidden;
            border-radius: 24px;
            background: rgba(255, 255, 255, 0.76);
            border: 1px solid rgba(23, 32, 51, 0.1);
            box-shadow: 0 18px 40px rgba(42, 53, 77, 0.1);
        }

        .item img {
            display: block;
            width: 100%;
            aspect-ratio: 4 / 3;
            object-fit: cover;
        }

        .item-content {
            padding: 18px;
        }

        .item h2 {
            margin: 0 0 8px;
            font-size: 22px;
        }

        .item p {
            margin: 0;
            color: #5d667a;
            line-height: 1.55;
        }

        footer {
            margin-top: 30px;
            color: #667086;
            text-align: center;
        }

        @media (max-width: 960px) {
            .hero {
                grid-template-columns: 1fr;
            }

            .hero-card {
                max-width: 560px;
                transform: none;
            }

            .gallery {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 760px) {
            .page {
                width: min(100% - 24px, 1120px);
                padding: 18px 0 28px;
            }

            .hero {
                gap: 20px;
                padding: 22px;
                border-radius: 24px;
                box-shadow: 0 18px 48px rgba(42, 53, 77, 0.13);
            }

            .eyebrow {
                margin-bottom: 10px;
                font-size: 12px;
                letter-spacing: 0.1em;
            }

            h1 {
                font-size: clamp(34px, 13vw, 54px);
                line-height: 1;
                letter-spacing: -0.05em;
            }

            .lead {
                margin-top: 16px;
                font-size: 16px;
                line-height: 1.55;
            }

            .hero-card {
                padding: 12px;
                border-radius: 20px;
            }

            .hero-card img {
                border-radius: 15px;
            }

            .hero-card p {
                margin: 12px 4px 2px;
                font-size: 14px;
                line-height: 1.4;
                overflow-wrap: anywhere;
            }

            .gallery {
                display: flex;
                gap: 14px;
                margin: 22px -12px 0;
                padding: 0 12px 10px;
                overflow-x: auto;
                scroll-snap-type: x mandatory;
                -webkit-overflow-scrolling: touch;
            }

            .item {
                flex: 0 0 min(82vw, 340px);
                border-radius: 20px;
                scroll-snap-align: start;
            }

            .item-content {
                padding: 16px;
            }

            .item h2 {
                font-size: 20px;
            }

            .item p {
                font-size: 15px;
            }

            footer {
                margin-top: 18px;
                font-size: 14px;
                line-height: 1.4;
            }
        }

        @media (max-width: 420px) {
            .hero {
                padding: 18px;
            }

            .item {
                flex-basis: 88vw;
            }
        }
    </style>
</head>
<body>
    <main class="page">
        <section class="hero">
            <div>
                <p class="eyebrow">Local Flask Demo</p>
                <h1>Простой сайт с медиа</h1>
                <p class="lead">
                    Это небольшое Flask-приложение в одном файле: маршрут, HTML-шаблон,
                    стили и галерея локальных изображений из папки static/media.
                </p>
            </div>
            <div class="hero-card">
                <img src="{{ url_for('static', filename='media/mountain.svg') }}" alt="Mountain sunrise illustration">
                <p>Запускается командой: flask --app main run</p>
            </div>
        </section>

        <section class="gallery" aria-label="Media gallery">
            {% for item in gallery %}
                <article class="item">
                    <img src="{{ url_for('static', filename=item.image) }}" alt="{{ item.title }} illustration">
                    <div class="item-content">
                        <h2>{{ item.title }}</h2>
                        <p>{{ item.description }}</p>
                    </div>
                </article>
            {% endfor %}
        </section>

        <footer>Made with Flask and local SVG media files.</footer>
    </main>
</body>
</html>
        """,
        gallery=gallery,
    )


if __name__ == "__main__":
    app.run(debug=True)
