<template>
    <div class="guestsContainer p-3 p-lg-5 d-flex flex-column my-auto">
        <h2 class="mb-5">Guests</h2>
        <b-table stacked :items="guests_data">
            <span slot="profile_picture" slot-scope="data" v-html="data.value">
            </span>
        </b-table>
    </div>
</template>

<script>
    /* eslint-disable no-console,array-callback-return */
    import axios from 'axios';
    import bTable from 'bootstrap-vue/es/components/table/table'

    export default {
        name: "aGuests",
        components: (
            bTable
        ),
        data() {
            return {
                guests: [],
                guests_data: []
            }
        },
        beforeCreate() {
            let Guest = class {
                constructor(profile_picture, name) {
                    this.profile_picture = profile_picture;
                    this.name = name;
                }
            };

            axios
                .get('/api/guest/')
                .then((response) => {
                    this.guests = response.data;

                    function createImg(href) {
                        return '<img src="' + href + '">'
                    }

                    this.guests.forEach((guest) => this.guests_data.push(new Guest(createImg(guest.profile_picture), guest.name)));

                    //remove duplicates by guest email
                    let temp = {};
                    for (let i = 0, len = this.guests_data.length; i < len; i++) {
                        temp[this.guests_data[i].email] = this.guests_data[i];
                    }
                    this.guests_data = [];
                    for (let key in temp) {
                        this.guests_data.push(temp[key])
                    }
                })
                .catch((e) => {
                    console.log(e);
                });
        },
    }
</script>