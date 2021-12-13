import Vue                  from "vue"
import VueRouter            from 'vue-router'
import Home                 from "./components/Home"
import ParticipantsForm     from "./components/ParticipantsForm"

Vue.use(VueRouter)

const routes = [
    { path : '/',                   component : Home },
    { path : '/participants-form',  component : ParticipantsForm },
]

export const router = new VueRouter({
    mode : 'history',
    routes
})