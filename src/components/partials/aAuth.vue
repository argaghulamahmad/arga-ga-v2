<template>
    <div>
        <section class="p-3 p-lg-5 d-flex flex-column" id="auth">
            <div class="div--wrapper">
                <b-jumbotron v-if="!user && !loading" bg-variant="white">
                    <template slot="header">
                        Contact Me
                    </template>
                    <template slot="lead">
                        Let me know you, please log in using your google account.
                        To see my personal details such as phone number and email, I need to know who you are.
                    </template>
                    <hr class="my-4">
                    <b-button size="sm" class="mx-auto my-2 my-sm-0" variant="primary" type="submit"
                              @click="signInWithGoogle"><i
                            class="fa fa-google"></i> Sign in with Google
                    </b-button>
                </b-jumbotron>
            </div>

            <div v-if="user">
                <b-container style="margin: 10px">
                    <b-row>
                        <b-col cols="8">
                            <p class="p--title">Hello, {{this.getUserName()}}. It was pleasure to meet you.</p>
                        </b-col>
                        <b-col cols="4">
                            <b-button id="btn-logout" @click="signOut" variant="danger" size="sm">
                                Sign Out
                            </b-button>
                        </b-col>
                    </b-row>
                </b-container>
                <aContactMe></aContactMe>
            </div>

            <aSpinner v-if="loading"></aSpinner>
        </section>
    </div>
</template>

<script>
    /* eslint-disable no-console */
    import {mapActions, mapGetters} from 'vuex';
    import firebase from 'firebase/app';
    import 'firebase/auth';
    import axios from 'axios';
    import bButton from 'bootstrap-vue/es/components/button/button';
    import bNavbar from 'bootstrap-vue/es/components/navbar/navbar';
    import bNavbarBrand from 'bootstrap-vue/es/components/navbar/navbar-brand';
    import bNavbarNav from 'bootstrap-vue/es/components/navbar/navbar-nav';
    import bJumbotron from 'bootstrap-vue/es/components/jumbotron/jumbotron';
    import aContactMe from '../sections/aContactMe';
    import aSpinner from '../partials/aSpinner';

    export default {
        name: 'aAuth',
        components: {
            aContactMe,
            aSpinner,
            bNavbar,
            bNavbarBrand,
            bNavbarNav,
            bButton,
            bJumbotron,
        },
        beforeCreate() {
            firebase.auth().onAuthStateChanged((user) => {
                let Guest = class {
                    constructor(name, email, profile_picture) {
                        this.name = name;
                        this.email = email;
                        this.profile_picture = profile_picture;
                    }
                };

                function getCookie(name) {
                    let cookieValue = null;
                    if (document.cookie && document.cookie !== '') {
                        let cookies = document.cookie.split(';');

                        let trim = (str) => {
                            return str.toString().replace(/^([\s]*)|([\s]*)$/g, '');
                        };

                        for (let i = 0; i < cookies.length; i++) {
                            let cookie = trim(cookies[i]);
                            // Does this cookie string begin with the name we want?
                            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                break;
                            }
                        }
                    }
                    return cookieValue;
                }

                if (user !== null && this.getUserEmail() === '') {
                    let guest = new Guest(user.displayName, user.email, user.photoURL);

                    let csrfToken = getCookie('csrftoken');
                    let headers = {"X-CSRFToken": csrfToken};

                    axios.post('/api/guest/', guest, {headers: headers}).then(function () {
                        console.log("Guest data has been saved successfully!");
                    })
                        .catch(function (error) {
                            console.log(error);
                        });
                }

                if (user) {
                    this.user = user;
                    this.actionUserName(this.user.displayName);
                    this.actionUserEmail(this.user.email);
                    this.actionUserPhotoUrl(this.user.photoURL);
                }
                this.loading = false;
            });
        },
        data() {
            return {
                loading: true,
                user: null,
            };
        },
        methods: {
            ...mapActions(['actionUserName', 'actionUserEmail', 'actionUserPhotoUrl']),
            ...mapGetters(['getUserName', 'getUserEmail', 'getUserPhotoUrl']),
            signInWithGoogle() {
                const provider = new firebase.auth.GoogleAuthProvider();
                firebase
                    .auth()
                    .signInWithRedirect(provider)
                    .then((result) => {
                        this.user = result.user;
                    })
                    .catch(error => console.log(error));
            },
            signOut() {
                firebase
                    .auth()
                    .signOut()
                    .then(() => {
                        this.user = null;
                        this.actionUserName('');
                        this.actionUserEmail('');
                        this.actionUserPhotoUrl('');
                    })
                    .catch(error => console.log(error));
            },
        },
    };
</script>
