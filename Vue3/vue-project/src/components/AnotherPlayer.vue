<!-- 
<template>
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    </head>
    <div id="player" @mouseover="toggleInfoBox" @mouseleave="toggleInfoBox">
      <div class="album">
        <div class="heart" :class="{ clicked: isHeartClicked }" @click="toggleHeart">
          <i class="fas fa-heart"></i>
        </div>
      </div>
      <div class="info" :class="{ up: infoBoxVisible }">
        <div class="progress-bar">
          <div class="time--current">1:25</div>
          <div class="time--total">-3:15</div>
          <div class="fill"></div>
        </div>
        <div class="currently-playing">
          <h2 class="song-name">Symphony</h2>
          <h3 class="artist-name">Clean Bandit ft. Zara Larsson</h3>
        </div>
        <div class="controls">
          <div class="option"><i class="fas fa-bars"></i></div>
          <div class="volume"><i class="fas fa-volume-up"></i></div>
          <div class="previous"><i class="fas fa-backward"></i></div>
          <div class="play" v-if="!isPlaying" @click="playMusic">
            <i class="fas fa-play"></i>
          </div>
          <div class="pause" v-if="isPlaying" @click="pauseMusic">
            <i class="fas fa-pause"></i>
          </div>
          <div class="next"><i class="fas fa-forward"></i></div>
          <div class="shuffle" :class="{ clicked: isShuffleClicked }" @click="toggleShuffle">
            <i class="fas fa-random"></i>
          </div>
          <div class="add"><i class="fas fa-plus"></i></div>
        </div>
      </div>
    </div>
  
  </template>
  
  <script>  
  export default {
    data() {
      return {
        isHeartClicked: false,
        isShuffleClicked: false,
        infoBoxVisible: false,
        isPlaying: false,
        audio: new Audio("http://music.dawnfoxes.com/_fxs_/_upls_/_sngs_/UK/clean_bandit-symphony-ft-zara_larsson.mp3"),
      };
    },
    methods: {
      toggleHeart() {
        this.isHeartClicked = !this.isHeartClicked;
      },
      toggleShuffle() {
        this.isShuffleClicked = !this.isShuffleClicked;
      },
      toggleInfoBox() {
        this.infoBoxVisible = !this.infoBoxVisible;
      },
      playMusic() {
        this.audio.play();
        this.isPlaying = true;
      },
      pauseMusic() {
        this.audio.pause();
        this.isPlaying = false;
      },
    },
  };
  </script>

<style scoped lang="scss">
$primary: #49654d;
$secondary: #8ba989;
$white: #ffffff;
$light: #c0cfb2;
$dark: #364f3c;

@import url("https://fonts.googleapis.com/css?family=Questrial");
$font: "Questrial", sans-serif;

html {
  min-height: 100%;
  display: grid;
}

body {
  background: linear-gradient(to bottom left, $light 10%, $secondary 80%);
  display: grid;
  overflow: hidden;
}

#player {
  background: $white;
  position: relative;
  margin: auto;
  width: 300px;
  height: 300px;
  overflow: hidden;
  border-radius: 5px;
  box-shadow: 5px 5px 15px rgba($dark, 0.4);
  -webkit-transition: all 0.5s ease-in-out;
  transition: all 0.5s ease-in-out;
  &:hover {
    transform: scale(1.05);
  }
}

.album {
  background: linear-gradient(rgba($dark, 0.25), rgba($primary, 0.55)),
    url("http://4.bp.blogspot.com/-pcPjBBdE_K8/U7v4oEX3M8I/AAAAAAAAD2I/6dWyzgiPzkQ/s1600/Clean+BAndit+Album+.jpg");
  background-repeat: no-repeat;
  background-size: 300px;
  width: 100%;
  height: 100%;
  border-radius: 5px;
  position: absolute;
}

.heart {
  position: absolute;
  right: 0;
  color: $white;
  margin: 10px;
  transition: all 0.4s ease;
}

.clicked {
  color: $primary;
  transform: scale(1.2);
  transition: all 0.4s ease;
}

.info {
  height: 115px;
  width: 100%;
  position: absolute;
  bottom: 0;
  background: rgba($white, 0.85);
  transform: translateY(35px);
  transition: all 0.5s ease-in-out;
}

.up {
  transform: translateY(0px);
}

.progress-bar {
  height: 5px;
  width: 73%;
  margin: 6% auto;
  background: lighten($light, 5%);
  border-radius: 10px;
  font-family: $font;
}

.fill {
  background-color: $secondary;
  width: 35%;
  height: 0.3rem;
  border-radius: 2px;
}

.time--current,
.time--total {
  color: $dark;
  font-size: 10px;
  position: absolute;
  margin-top: -2px;
}

.time--current {
  left: 15px;
}

.time--total {
  right: 15px;
}

.currently-playing {
  text-align: center;
  margin-top: -3px;
}

.song-name,
.artist-name {
  font-family: $font;
  text-transform: uppercase;
  margin: 0;
}

.song-name {
  font-size: 0.8em;
  letter-spacing: 3px;
  color: $dark;
}

.artist-name {
  font-size: 0.6em;
  letter-spacing: 1.5px;
  color: lighten($dark, 15%);
  margin-top: 5px;
}

.controls {
  display: flex;
  align-items: center;
  font-size: 0.8em;
  justify-content: center;
  color: $secondary;
  .play,
  .pause {
    margin: 15px 25px;
    color: darken($secondary, 10%);
  }
  .option {
    left: 10px;
    position: absolute;
    font-size: 0.8em;
  }
  .add {
    right: 10px;
    position: absolute;
    font-size: 0.8em;
  }
  .volume {
    margin-right: 30px;
    font-size: 0.8em;
  }
  .shuffle {
    margin-left: 30px;
    font-size: 0.8em;
  }
}

.play,
.pause,
.next,
.previous,
.option,
.add,
.volume,
.shuffle {
  transition: all 0.5s ease;
  &:hover {
    color: lighten($dark, 15%);
  }
}

footer {
  position: absolute;
  bottom: 0;
  right: 0;
  text-align: center;
  font-size: 0.5em;
  text-transform: uppercase;
  padding: 10px;
  color: $primary;
  letter-spacing: 3px;
  font-family: $font;
  a {
    color: #ffffff;
    text-decoration: none;
    &:hover {
      color: $primary;
    }
  }
}
</style> -->