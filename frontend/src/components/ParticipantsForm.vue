<template>
    <div class="participants-form">

        <!-- HEADER -->
        <div class="participants-form-header">
            <router-link class="home-button" to="/">
                Anasayfaya Git
            </router-link>
            <div class="add-participant">
                <a
                    href    ="#"
                    @click  ="addParticipant()">
                    + Katılımcı Ekle
                </a>
            </div>
        </div>
        <div class="fix-style"></div>
        
        <!-- FORM -->
        <div
            class     ="participants-form-list"
            v-for     ="(participant, index) in participants"
            :key      ="index">

            <div class="participants-number">
                <span class="p-info-text"> {{ index + 1}}. KATILIMCI BİLGİLERİ </span>
                <div class="participant-actions">
                    <button
                        class           ="remove-participant"
                        style           ="cursor: pointer;"
                        @click          ="removeParticipant(index)"
                    >
                            <span>Katılımcıyı Sil</span>
                    </button>
                    <button
                        @click="viewToggleParticipant(participant)"
                        class="hide-participant">
                        <span> {{ toggleVisibleText(participant) }} </span>
                    </button>
                </div>
            </div>
            <div class="participant-form" v-if="participant.isVisible">
                <div class="default-form">
                    <input
                        v-model         ="participant.name"
                        type            ="text"
                        name            ="name"
                        placeholder     ="Katılımcı Adı"
                        class           ="nameInput"
                    />
                    <input
                        v-model         ="participant.email"
                        type            ="text"
                        name            ="email"
                        placeholder     ="E-posta"
                        class           ="nameInput"
                    />
                </div>
                <div class="form-with-address">
                    <textarea
                        class           ="nameInput text-area"
                        v-if            ="addressStatus"
                        v-model         ="participant.address"
                        name            ="address"
                        placeholder     ="Adres"
                    />
                </div>
            </div>
        </div>

        <!-- FOOTER -->
        <div class="footer">
            <div class="add-address">
                <div class="add-address-btn">
                    <button
                        :class  ="[{'active-class' : addressStatus}, 'add-address-btn-item']" 
                        @click  ="selectAddAddress(true)">
                        + Adres Bilgisi Ekle
                    </button>
                    <button
                        :class  ="[{'active-class' : !addressStatus}, 'add-address-btn-item']" 
                        @click  ="selectAddAddress(false)">
                        Eklemeden Devam Et
                    </button>
                </div>

                <div class="create-button">
                    <a 
                        href    ="#" 
                        @click  ="createDraw()" 
                        class   ="create-button-item"
                    >Çekilişi Yap!</a
                    >
                </div>

                <p class="info-text">
                    Eşleşmeler her bir katılımcının
                    mail adresine gönderilecektir.
                </p>
            </div>
        </div>


        <!-- FINALLY MODAL -->
        <modal
            name        ="finally-modal"
            :min-width  ="200"
            :min-height ="200"
            :scrollable ="true"
            :reset      ="true"
            :width      ="screenWidth"
            height      ="auto"
        >
            
            <div class="finally-content">
                <span @click="closeModal()" class="close-modal">x</span>
                <img
                    class   ="finally-content-img" 
                    src     ="src/assets/img/congrats.png" 
                >
                <p class="finally-content-title">
                    Yılbaşı çekilişiniz başarı ile gerçekleşti!
                </p>
                <p class="finally-content-text">
                    Lütfen E-Mail hesabınınızı kontrol ediniz. Spam kutusunu kontrol etmeyi unutmayınız.
                </p>

                <div class="finally-content-buttons">
                    <button
                        onclick="window.open('https://github.com/selamet/online-yilbasi-cekilisi')">
                        <i class="fab fa-github"></i>
                        GitHub
                    </button>

                    <button
                        onclick="window.open('mailto:yeniyilcekilisi@gmail.com')">
                        <i class="fas fa-envelope"></i>
                        E-Mail
                    </button>
                    
                    <button
                        onclick="window.open('https://kreosus.com/yilbasicekilisi')">
                        <i class="fas fa-gift"></i>
                        Bağış
                    </button>
                </div>

            </div>
        </modal>

        <!-- VALIDATION MODAL -->
        <modal
            name        ="validation-modal"
            :min-width  ="200"
            :min-height ="200"
            :scrollable ="true"
            :reset      ="true"
            :width      ="screenWidth"
            height      ="auto"
        >
            
            <div class="validation-content" >
                <span @click="closeModalValidation()" class="close-modal">x</span>
                <div v-if="getEmptyField.length || getMailNotValid.length">
                    <div class="validation-content-title">
                        <div class="image">
                            <img src="src/assets/img/warning.png">
                        </div>
                        <h3 v-if="getEmptyField.length || getMailNotValid.length">
                            Aşağıda belirtilen alanları kontrol edin
                        </h3>
                    </div>
                    <div 
                        v-if    ="getEmptyField.length" 
                        class   ="validation-empty-field">
                        <h5>Boş Bırakılan Alanlar</h5>
                        <div 
                            class   ="list" 
                            v-for   ="(item, index) in getEmptyField" 
                            :key    ="index">
                            <span class="item">{{ item }}</span>
                        </div>
                    </div>
                    <div 
                        v-if    ="getMailNotValid.length" 
                        class   ="validation-mail-valid">
                        <h5>Geçersiz E-Mail Girilen Alanlar</h5>
                        <div 
                            class   ="list" 
                            v-for   ="(item, index) in getMailNotValid" 
                            :key    ="index">
                            <span class="item">{{ item }}</span>
                        </div>
                    </div>
                </div>
                <div v-else-if="!getNumberOfParticipantsOnePerson">
                    <div class="validation-content-title">
                        <div class="image">
                            <img src="src/assets/img/warning.png">
                        </div>
                        <h3>
                            Tek başına çekiliş yapamazsın
                        </h3>
                    </div>
                </div>
            </div>
        </modal>
    </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      screenWidth       : '',
      participants      : [{id: 1, isVisible: true, name: "", email: ""}],
      mailCheck         : true,
      addressStatus     : false,
      formValidation    : false
    };
  },
  created() {
    this.screenWidth = screen.width < 750
        ? "90%"
        : "70%"
  },
  computed: {
    getEmptyField() {
        return this.validationCheck().hasEmptyField
    },
    getMailNotValid() {
        return this.validationCheck().hasMailNotValid
    },
    getNumberOfParticipantsOnePerson() {
        return this.validationCheck().isNumberOfParticipantsOnePerson
    },
  },
  methods: {
    addParticipant() {
      let id = this.participants.length + 1;
      this.addressStatus
        ? this.participants.push({
          id        : id,
          isVisible : true,
          name      : '',
          email     : '',
          address   : '',
        })
        : this.participants.push({
          id        : id,
          isVisible : true,
          name      : '',
          email     : '',
        })
    },
    removeParticipant(index) {
        if (this.participants.length > 1) this.participants.splice(index, 1);
    },
    viewToggleParticipant(item) {
        item.isVisible = !item.isVisible
    },
    toggleVisibleText(item) {
        return item.isVisible
          ? 'Gizle'
          : 'Göster'
    },
    selectAddAddress(hasAddress) {
        this.addressStatus = hasAddress;
        this.addressStatus
            ? this.participants.map(item => item.address = '')
            : this.participants.map(item => delete item.address)
    },
    showFinally() {
        this.$modal.show("finally-modal");
    },
    hideFinally() {
        this.$modal.hide("finally-modal");
    },
    showValidation() {
        this.$modal.show("validation-modal");
    },
    hideValidation() {
        this.$modal.show("validation-modal");
    },
    closeModal() {
        this.$modal.hide("finally-modal");
    },
    closeModalValidation() {
        this.$modal.hide("validation-modal");
    },
    validationCheck() {
        const reg = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/
        const participantsLength = this.participants.length

        let hasEmptyField = []
        let hasMailNotValid = []
        let isNumberOfParticipantsOnePerson = false

        this.participants.map((participant, index) => {
            if (!reg.test(participant.email) && participant.email) {
                hasMailNotValid.push({
                    label   : `${index+1}. Katılımcı`
                })
            }

            if (!participant.name || !participant.email) {
                hasEmptyField.push({
                    label   : `${index+1}. Katılımcı`
                })
            }
        })

        isNumberOfParticipantsOnePerson = participantsLength === 1
            ? false
            : true

        const isValid = !hasEmptyField.length && !hasMailNotValid.length && isNumberOfParticipantsOnePerson
        
        this.formValidation = isValid
            ? true
            : false 

        return {
            hasEmptyField   : hasEmptyField.map(item => item.label),
            hasMailNotValid : hasMailNotValid.map(item => item.label),
            isNumberOfParticipantsOnePerson
        }
    },
    createDraw() {
        this.validationCheck();
        if (!this.formValidation) {
            this.showValidation()
            return
        }

        this.participants.map(item => delete item.isVisible)
        if (this.formValidation) {
            axios.post('https://api.yilbasicekilisi.online', this.participants).then((response) => {
                this.showFinally();
                this.addressStatus  = false;
                this.participants   = [{ id: 1, name: '', email: '', isVisible:true }];
            });
        }
    },
  },

};
</script>


<style>

.participants-form {
    background: #F3F4F6;
    min-height: 100vh;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
}

.participants-form-header {
    position: fixed;
    background: #F3F4F6;
    width: 100%;
    padding-left: 15%;
    padding-right: 15%;
    display: flex;
    height: 100px;
    align-items: center;
    justify-content: space-between;
}

.fix-style {
    display: block;
    height: 100px;
    width: 100%;
}
.add-participant {
    width: auto;
    top: 0;
    right: 0;
    display: flex;
    align-items: center;
}

.add-participant a {
    border: 1px solid #666666;
    border-radius: 4px;
    font-size: 12px;
    font-weight: 600;
    padding: 5px 10px;
    height: 40px;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    background: #3A4149;
    color: white;
}

.home-button {
  border: 1px solid #666666;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 600;
  color: #3A4149;
  padding: 10px;
  height: 40px;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  margin-right: 20px;
}

.participants-form-list {
    width: 70%;
    display: flex;
    flex-direction: column;
    align-items: center;
    background: white;
    box-shadow: 0 1px 3px 0 rgb(0 0 0 / 10%), 0 1px 2px 0 rgb(0 0 0 / 6%);
    padding: 20px;
    border-radius: 4px;
    margin-bottom: 20px;
}

.participants-number {
    display: flex;
    width: 100%;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
}

.participant-actions {
    display: flex;
    flex-wrap: nowrap;
    justify-content: flex-end;
}

.remove-participant {
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 4px;
  padding: 5px 10px;
  cursor: pointer;
  background: #ec5161;
  border: 1px solid white;
  height: 40px;
  border: none;
  width: 120px;
  text-transform: capitalize;
}

.remove-participant span {
  color: #fff;
  font-size: 12px;
  font-weight: 600;
  letter-spacing: .4px;
}

.hide-participant {
    height: 40px;
    width: 60px;
    border: none;
    background: none;
    display: flex;
    align-items: center;
    justify-content: center;
    outline: none;
    color: #3A4149;
}

.hide-participant span {
    color: #3A4149;
}

.participants-number .p-info-text {
    font-weight: 600;
    font-size: 12px;
    color: #3A4149;
}

.participant-form {
    width: 100%;
}

.default-form {
  display: flex;
  width: 100%;
  align-items: center;
  justify-content: space-between;
}

.default-form input {
    width: calc(50% - 10px);
}

.default-form input::placeholder, textarea::placeholder {
  color: #18181870;
  opacity: 1;
}

.form-with-address {
  width: 100%;
  display: flex;
  margin-top: 20px ;
}

/* FOOTER */
.footer {
  /* background: #fff; */
  height: auto;
  text-align: center;
  width: 70%;
  display: flex;
}

.add-address {
  width: 100%;
}

.add-address-btn {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}

.add-address-btn-item {
  background: #ebebeb;
  color: #3A4149;
  border: none;
  width: 90px;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: .5px;
  width: 50%;
  height: 50px;
}

.add-address-btn-item:first-child {
  border-top-left-radius: 4px;
  border-bottom-left-radius: 4px;
}

.add-address-btn-item:last-child {
  border-top-right-radius: 4px;
  border-bottom-right-radius: 4px;
}

.create-button {
  margin-top: 20px;
  margin-bottom: 10px;
}

.create-button-item {
  width: 100%;
    background: #2EA45F;
    height: 50px;
    border-radius: 4px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    font-size: 16px;
    letter-spacing: 1px;
    font-weight: 500;
}

.create-button-item:hover {
    color: white;
    box-shadow: 0 0 10px rgba(0,0,0,.2);
}

.info-text {
  color: #3A4149;
  font-weight: 400;
  opacity: 0.6;
}

/* FINALLY CONTENT */

.finally-content {
    padding-top: 80px;
    padding-bottom: 80px;
}

.finally-content-img {
    width: 150px;
    height: 150px;
}

.finally-content-title {
    margin-top: 20px;
    font-size: 22px;
    font-weight: 600;
}

.finally-content-text {
    padding-left: 20px;
    padding-right: 20px;
    margin-top: 0px;
    font-size: 18px;
    font-weight: 300;
    opacity: .8;

}

.finally-content-buttons {
    display: flex;
    width: 100%;
    height: 50px;
    justify-content: space-evenly;
    align-items: center;
    margin-bottom: 20px;
    margin-top: 10px;
}

.finally-content-buttons button {
    border: none;
    height: 50px;
    width: 150px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: 400;
    font-size: 16px;
    border-radius: 4px;
}

.finally-content-buttons i {
    padding-right: 8px;
    opacity: .9;
    padding-bottom: 3px;
}

/* VALIDATION CONTENT */

.validation-content {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    align-items: center;
    padding: 60px 0;
}

.validation-content-title {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
}

.validation-content-title .image {
    width: 100%;
    display: flex;
    justify-content: center;
}

.validation-content-title .image img {
    width: 100px;
    height: 100px;
}

.validation-empty-field, .validation-mail-valid {
    display: flex;
    width: 100%;
    justify-content: center;
    flex-wrap: wrap;
    align-items: center;
    margin-top: 10px;
}

.validation-empty-field h5, .validation-mail-valid h5 {
    width: 100%;
    text-align: center;
    font-weight: 300;
}

.validation-empty-field .list, .validation-mail-valid .list {
    margin: 10px 0;
}

.validation-empty-field .list .item {
    padding: 10px 15px;
    font-size: 12px;
    background: #EFEFEF;
    color: #4C5359;
    font-weight: 500;
    border-radius: 4px;
    margin: 5px;
}

.validation-mail-valid .list .item {
    padding: 10px 15px;
    font-size: 12px;
    background: #EFEFEF;
    color: #4C5359;
    font-weight: 500;
    border-radius: 4px;
    margin: 5px;
}

.close-modal {
    position: absolute;
    top: 5px;
    right: 5px;
    height: 40px;
    width: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    color: #333333;
    border-radius: 50%;
    padding-bottom: 2px;
    cursor: pointer;
}

/* ############################## */

.active-class {
  background: #3A4149!important;
  outline: none!important;
  color: white!important;
}

.start-draw {
  width: 80%;
  height: 50px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 16px;
  background: #38c172;
  color: white;
  font-weight: 600;
  letter-spacing: 1px;
  border-radius: 4px;
  height: 60px;
}

.draw-button {
  width: 100%;
  border: none;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 15px 0;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 900;
  letter-spacing: 1px;
  background: #e91327;
  color: white;
}

.nameInput {
    border: 1px solid lightgray;
    width: 40%;
    margin: 0;
    padding: 5px 10px;
    height: 50px;
    border-radius: 4px;
    color: #3A4149;
    background: #f4f7fa;
    display: block;
    border: 1px solid #d2dae1;
    background-color: #f4f7fa !important;
    outline: none;
    padding: 0 14px;
    font-size: 16px;
}

.text-area {
  width: 100%;
  display: flex;
  height: auto;
  /* margin: 20px; */
  width: 100%;
}

.list-fix {
  display: flex;
  widows: 100%;
  height: 30px;
}

.header {
  margin: 0;
  padding: 0;
  margin-bottom: 30px;
  height: 100px;
  background-color: #fff;
  box-shadow: 0 5px 10px #f4f7fa;
  display: flex;
  justify-content: center;
  align-items: center;
}

.header h4 {
  margin-top: 10px;
  font-size: 42px;
  color: #3A4149;
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
  color: #3A4149;
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
  flex-wrap: wrap;
  /* margin: 2px 10px 0px 10px; */
  align-items: center;
  justify-content: center;
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

@media (max-width: 991px) {

    .participants-form-header {
        width: 100%;
        padding-left: 5%;
        padding-right: 5%;
    }

    .participants-form-list {
        width: 90%;
    }

    .footer {
        width: 90%;
    }

    .add-participant {
        width: 50%;
        top: 80px;
    }

    .home-button {
        width: 50%;
        font-size: 10px;
        justify-content: center;
    }
    .add-participant a {
        background: #3A4149;
        color: white;
        width: 100%;
        font-size: 10px;
        justify-content: center;
    }

    .remove-participant {
        width: 70%;
        max-width: 120px;
    }

    .remove-participant span {
        font-size: 11px;
        white-space: nowrap;
    }

    .hide-participant {
        width: 30%;
    }

    .hide-participant span {
        font-size: 14px;
    }

    .header {
        height: 160px;
    }

    .header h4 {
        font-size: 32px;
    }

    .add-address-btn-item {
        font-size: 12px;
    }

    .participants-number {
        display: flex;
        flex-wrap: wrap;
    }

    .p-info-text {
        display: flex;
        width: 50%;
    }

    .participant-actions {
        width: 50%;
    }

    .default-form {
        display: flex;
        flex-wrap: wrap;
    }

    .default-form input {
        width: 100%;
    }

    .default-form input:nth-of-type(1) {
        margin-bottom: 20px;
    }

    /* VALIDATION CONTENT */
    
    .validation-content .validation-content-title h3{
        font-size: 18px;
        justify-content: center;
    }

    .validation-content .validation-content-title img{
        width: 100px;
        height: 100px;
    }

    .finally-content {
        padding-top: 40px;
        overflow-y: auto;
    }

    .finally-content-title {
        font-size: 18px;
        padding-left: 10px;
        padding-right: 10px;
    }

    .finally-content-text {
        font-size: 14px;
        padding-left: 10px;
        padding-right: 10px;
    }

    .finally-content-buttons {
        display: flex;
        flex-wrap: wrap;
        height: 120px;
    }

    .finally-content-buttons button{
        width: 60%;
        margin: 5px 0;
    }

    .finally-content-buttons button:last-child{
        margin-bottom: 40px;
    }
}

</style>
