import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Entertainment Center</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background-color: black;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }

        .navbar {
            background-color: #9C27B0;
            color: white;
        }

        .navbar .navbar-brand {
            color: white;
        }

        .movie-tiles-container {
            display: flex;
            flex-flow: row wrap;
            padding-left: 20px;
            padding-right: 20px;
        }

        .section-title {
            flex: 1 1 100%;
            color: white;
            font-size: 16px;
            font-weight: bold;
            padding: 20px;
            background-color: rgba(255,255,255,0.1);
        }

        .movie-tile {
            padding: 20px;
            color: white;
            transition: width 300ms ease-in;
            flex: 0 1 220px;
            display: flex;
            flex-flow: row nowrap;
        }

        .movie-tile.open {
            background-color: rgba(255,255,255,0.10);
        }

        .movie-tile:hover {
            background-color: rgba(255,255,255,0.15);
            cursor: pointer;
        }


        .movie-tile .movie-title {
            font-size: 14px;
            max-width: 220px;
        }

        .movie-tile .movie-tile-heading {
            max-width: 220px;
        }

        .movie-tile .movie-tile-detail {
            display: none;
            padding-left: 20px;
            padding-right: 20px;
            flex: 1 1 auto;
        }

        .movie-tile.open .movie-tile-detail {
            display: block;
        }

        .movie-tile.open {
            flex: 1 0 100%;
        }

        .btn-watch-trailer {
            background-color: #9C27B0;
            color: white;
        }

        .btn-watch-trailer:hover {
            background-color: #AB47BC;
            color: white;
        }

        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        $(document).on('click', '.movie-tile', function (event) {

            if($(this).hasClass('open')){
                $(this).removeClass('open');
            }else{
                $('.movie-tile').removeClass('open');
                $(this).toggleClass('open');
                $('html, body').animate({
                    scrollTop: $(this).offset().top - 80
                }, 1000);
            }

        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.btn-watch-trailer', function (event) {

            event.stopPropagation();

            $('#trailer').modal({show: true});

            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));


        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container-fluid">
      <div class="navbar navbar-fixed-top" role="navigation">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Entertainment Center</a>
          </div>
      </div>
    </div>

    <div class="movie-tiles-container">
      <div class="section-title">Favorite Movies</div>
      {favorite_movie_tiles}
      <div class="section-title">Popular Movies</div>
      {popular_movie_tiles}
    </div>    

  </body>
</html>
'''

#
# A single movie entry html template
movie_tile_content = '''
<div class="movie-tile">
    <div class="movie-tile-heading">
        <img src="{poster_image_url}" width="220" height="342">
        <h3 class="movie-title">{movie_title}</h3>
    </div>
    <div class="movie-tile-detail">
        <p>{overview}</p>
        <p><small>Released {release_date}</small></p>
        {trailer_button}
    </div>
</div>
'''

trailer_button_content = '''
<button type="button" 
        data-trailer-youtube-id="{trailer_youtube_id}" 
        class="btn btn-watch-trailer">
    Watch Trailer
</button>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:

        if movie.trailer_youtube_url != None:
            # Extract the youtube ID from the url
            youtube_id_match = re.search(
                r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
            youtube_id_match = youtube_id_match or re.search(
                r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
            trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                                  else None)
            trailer_button = trailer_button_content.format(
                trailer_youtube_id=trailer_youtube_id
            )
        else:
            trailer_button = ""

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_button=trailer_button,
            overview=movie.overview.encode('utf-8'),
            release_date=movie.release_date
        )
    return content


def open_movies_page(favorite_movies, popular_movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        favorite_movie_tiles=create_movie_tiles_content(favorite_movies),
        popular_movie_tiles=create_movie_tiles_content(popular_movies)
    )

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
