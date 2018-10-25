<template>
    <div class="guestsContainer p-3 p-lg-5 d-flex flex-column my-auto">
        <h2 class="mb-5">Guests</h2>
        <b-table :items="guests_data">
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
                constructor(profile_picture, name, email) {
                    this.profile_picture = profile_picture;
                    this.name = name;
                    this.email = email;
                }
            };

            axios
                .get('/api/guest/')
                .then((response) => {
                    this.guests = response.data;

                    function createImg(href) {
                        return '<img src="' + href + '">'
                    }

                    this.guests.forEach((guest) => this.guests_data.push(new Guest(createImg(guest.profile_picture), guest.name, guest.email)))
                })
                .catch((e) => {
                    console.log(e);
                });
        },
    }
</script>

<style scoped>

</style>