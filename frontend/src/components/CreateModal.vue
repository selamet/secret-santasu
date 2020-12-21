<template>
  <div>
    <a href="#" @click.prevent="show" class="hvr-radial-out button-theme"
    >Çekiliş Yap!</a
    >
    <modal
      name="create-modal"
      :min-width="200"
      :min-height="200"
      :scrollable="true"
      :reset="true"
      :width="screenWidth"
      height="auto"
    >
      <div class="header">
        <h4>Mutlu Yıllar...</h4>
      </div>

      <div style="margin-top: 10px" class="participants">
        <div
          class="participants-form-list"
          v-for="(participant, index) in participants"
          :key="index"
        >
          <div class="participant-form">
            <input
              v-model="participant.name"
              type="text"
              name="name"
              placeholder="Katılımcı Adı"
              class="nameInput"
            />
            <input
              v-model="participant.email"
              type="text"
              name="email"
              placeholder="E-posta"
            />
            <i
              class="glyphicon glyphicon-remove"
              style="cursor: pointer;"
              @click="removeParticipant(index)"
            ></i>
          </div>
          <hr>
        </div>
      </div>
      <div class="footer">
        <p>
          <span style="color: #e91327">> </span>Eşleşmeler her bir katılımcının
          mail adresine gönderilecektir.
        </p>
        <div class="buttons">
          <a
            href="#"
            @click="addParticipant()"
            class="hvr-radial-out button-theme"
          >Katılımcı Ekle</a
          >
          <a href="#" @click="createDraw()" class="hvr-radial-out button-theme"
          >Çekilişi Yap!</a
          >
        </div>
      </div>
    </modal>
    <modal
      name="finally-modal"
      :min-width="200"
      :min-height="200"
      :scrollable="true"
      :reset="true"
      :width="screenWidth"
      height="auto"
    >
      <div class="header">
        <h4>Mutlu Yıllar...</h4>
      </div>

      <div style="margin-top: 10px" class="finally-content">
        <p>Tebrikler yılbaşı çekilişiniz başarı ile gerçekleşti. Lütfen mail kutunuzu kontrol ediniz. <br> <small>(Spam
          kutunuzu kontrol etmeyi unutmayınız :)</small></p>
        <img src="src/assets/img/gift.png" alt="" height="60%" width="60%">

        <p>2021 yılında neşeniz, sağlığınız, mutluluğuz ve huzurunuz eksik olmasın. Mutlu yıllar dileriz.</p>
        <p class="logos">

          <span
            onclick="window.open('https://github.com/selamet/online-yilbasi-cekilisi')"
          ><i class="fab fa-github"></i></span>

          <span
            onclick="window.open('mailto:yeniyilcekilisi@gmail.com')"
          ><i class="fas fa-envelope"></i></span>
          <span
            onclick="window.open('https://kreosus.com/yilbasicekilisi')"
          ><i class="fas fa-gift"></i></span>

        </p>

      </div>
      <div class="last-message">
        <p>
          Projeyi
          <span
            onclick="window.open('https://twitter.com/selametsamli')"
          >Selam Şamlı</span
          >
          ve
          <span
            onclick="window.open('https://twitter.com/ilteriskeskin')"
          >Ali İlteriş Keskin</span
          >
          haftasonu projesi olarak geliştirmiştir. Proje açık
          kaynaktır ve isteyen herkes bu projeye katkıda bulunabilir.
        </p>
        <p>
          Eğer yılbaşı bize de hediye almak isterseniz <span
          onclick="window.open('https://twitter.com/ilteriskeskin')"
        >buradan </span> gönderebilirsiniz :)<br>

        </p>
      </div>
    </modal>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      screenWidth: '',
      participants: [{id: 1, name: "", email: ""}],
      mailCheck: true
    };
  },
  created() {
    console.log(screen.width)
    if (screen.width < 750) {
      this.screenWidth = "90%"
    } else {
      this.screenWidth = "60%"
    }
  },
  methods: {
    show() {
      this.$modal.show("create-modal");
    },
    hide() {
      this.$modal.hide("create-modal");
    },
    showFinally() {
      this.$modal.show("finally-modal");
    },
    hideFinally() {
      this.$modal.hide("finally-modal");
    },
    addParticipant() {
      let id = this.participants.length + 1;
      this.participants.push({
        id: id,
        name: "",
        email: "",
      });
    },
    removeParticipant(index) {
      this.participants.splice(index, 1);
    },
    findEmptyField() {
      const reg = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/
      let arr = this.participants.filter(function (a) {
        if (!reg.test(a.email) && a.email !== "") {
          alert(`${a.email} Geçerli bir eposta adresi olarak gözükmüyor.`)
          this.mailCheck = false;
        }
        if (!(a.name === "" || a.email === "")) {
          return a;
        }
      });
      return arr;
    },
    createDraw() {
      let arr = this.findEmptyField();
      if (arr && arr.length > 0 && this.mailCheck) {
        axios.post("http://127.0.0.1:5000", arr).then((response) => {
          this.hide();
          this.showFinally();
        });
      } else if (arr.length === 0) {
        alert("Lütfen Tüm alanları doldurun")
      }

    },
  },

};
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
  font-family: "Great Vibes", cursive;
  font-weight: 300;
}

@import url(https://fonts.googleapis.com/css?family=Roboto:400,300,500);
*:focus {
  outline: none;
}

img {
  object-fit: contain;
}

body {
  margin: 0;
  padding: 0;
  background: #ddd;
  font-size: 16px;
  color: #222;
  font-family: "Roboto", sans-serif;
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

.finally-content {
  height: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;


}

.finally-content p {
  color: #222222;
  text-align: center;
}

.logos span i {
  color: #222222;
  font-size: 24px;
  margin: 0 5px 0 5px;
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

.last-message {
  background-color: #ddd;
  height: auto;
  display: flex;
  align-items: center;
  justify-items: center;
  flex-direction: column;
}

.last-message p {
  color: #222222;
  font-size: 13px;
  margin: 10px 10px 0 10px;
  text-align: center;
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
  border-bottom: 1px solid #aaa;
  font-family: "Roboto", sans-serif;
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
  color: #fff;
  font-family: "Roboto", sans-serif;
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

@media only screen and (max-width: 755px) {
  .participant-form {
    flex-direction: column;
  }

  .participant-form input {
    width: 100%;
  }
}
</style>
