<template>
  <div>
    <a href="" @click.prevent="show" class="hvr-radial-out button-theme">Çekiliş Yap!</a>
    <modal
      :height="500"
      :width="700"
      name="create-modal">
      <div class="header">
        <h4>Mutlu Yıllar...</h4>
      </div>

      <div style="margin-top:10px" class="participants">
        <div class="participants-form-list" v-for="(participant,index) in participants" :key="index">

          <div class="participant-form">
            <span style="color: #3a4149">{{ participant.id }}.</span>
            <input v-model="participant.name" type="text" name="name" placeholder="Katılımcı Adı"/>
            <input v-model="participant.email" type="text" name="email" placeholder="E-posta"/>

          </div>
        </div>


      </div>
      <div class="footer">
        <p><span style="color: #e91327">> </span>Eşleşmeler her bir katılımcının mail adresine gönderilecektir.</p>
        <div class="buttons">
          <a href="#" @click="addParticipant()" class="hvr-radial-out button-theme">Katılımcı Ekle</a>
          <a href="#" @click="createDraw()" class="hvr-radial-out button-theme">Çekilişi Yap!</a>
        </div>
      </div>

    </modal>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      participants: [
        {id: 1, name: '', email: ''},

      ]
    }
  },
  methods: {
    show() {
      this.$modal.show('create-modal');
    },
    hide() {
      this.$modal.hide('create-modal');
    },
    addParticipant() {
      let id = this.participants.length + 1
      this.participants.push({
        id: id, name: '', email: ''
      })
    },
    findEmptyField() {
      let arr = this.participants.filter(function (a) {
        if (!(a.name === '' || a.email === '')) {
          return a
        }
      })
      return arr
    },
    createDraw() {
      let arr = this.findEmptyField()
      axios.post("http://127.0.0.1:5000", arr).then(response => {
        console.log(response)
      });
    }
  }


}
</script>


<style>
.header {
  margin: 0;
  padding: 0;
  background-color: #e91327;
  height: 60px;
  display: flex;
  justify-content: center;
  align-items: center;

}

.header h4 {
  margin-top: 10px;
  font-size: 42px;
  color: #ffffff;
  font-family: 'Great Vibes', cursive;
  font-weight: 300;
}


@import url(https://fonts.googleapis.com/css?family=Roboto:400,300,500);
*:focus {
  outline: none;
}

body {
  margin: 0;
  padding: 0;
  background: #DDD;
  font-size: 16px;
  color: #222;
  font-family: 'Roboto', sans-serif;
  font-weight: 300;
}

h1 {
  margin: 0 0 20px 0;
  font-weight: 300;
  font-size: 28px;
}

.participants {
  height: 300px;
  overflow: scroll;

}

.participant-form {
  display: flex;
  margin: 2px 10px 0px 10px;
  align-items: center;
  justify-content: center;

}

.participant-form input {
  margin: 3px 10px 0px 10px;
}

.footer {
  background-color: #ddd;
  height: 150px;
  text-align: center;
}


.buttons {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
}


.buttons a {
  margin-right: 10px;
}

input[type="text"],
input[type="password"] {
  display: block;
  box-sizing: border-box;
  margin-bottom: 20px;
  padding: 4px;
  width: 220px;
  height: 32px;
  border: none;
  border-bottom: 1px solid #AAA;
  font-family: 'Roboto', sans-serif;
  font-weight: 400;
  font-size: 15px;
  transition: 0.2s ease;
}

input[type="text"]:focus,
input[type="password"]:focus {
  border-bottom: 2px solid #e91327;
  color: black;
  transition: 0.2s ease;
}

input[type="submit"] {
  margin-top: 28px;
  width: 120px;
  height: 32px;
  background: #e91327;
  border: none;
  border-radius: 2px;
  color: #FFF;
  font-family: 'Roboto', sans-serif;
  font-weight: 500;
  text-transform: uppercase;
  transition: 0.1s ease;
  cursor: pointer;
}

input[type="submit"]:hover,
input[type="submit"]:focus {
  opacity: 0.8;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
  transition: 0.1s ease;
}

input[type="submit"]:active {
  opacity: 1;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.4);
  transition: 0.1s ease;
}


</style>
