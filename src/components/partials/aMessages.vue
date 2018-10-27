<template>
    <div class="messagesContainer p-3 p-lg-5 d-flex flex-column my-auto">
        <h2 class="mb-5">Messages</h2>
        <b-table stacked :items="messages">
        </b-table>
    </div>
</template>

<script>
    /* eslint-disable no-console,array-callback-return */
    import axios from 'axios';
    import bTable from 'bootstrap-vue/es/components/table/table'

    export default {
        name: "aMessages",
        components: (
            bTable
        ),
        data() {
            return {
                messages: []
            }
        },
        beforeCreate() {
            let Message = class {
                constructor(sender_name, subject, body, level) {
                    this.sender_name = sender_name;
                    this.subject = subject;
                    this.body = body;
                    this.level = level;
                }
            };

            axios
                .get('/api/messages/')
                .then((response) => {
                    response.data.forEach((message) => this.messages.push(new Message(message.sender_name,
                        message.subject, message.body, message.level)))
                })
                .catch((e) => {
                    console.log(e);
                });
        },
    }
</script>