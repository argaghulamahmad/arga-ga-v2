<template>
    <div>
        <div class="weight">
            <bCard no-body>
                <b-tabs nav-class="mx-auto" card>
                    <b-tab title="Calendly" active>
                        <br>
                        <aCalendly></aCalendly>
                    </b-tab>
                    <b-tab title="Leave a message">
                        <br>
                        <aSendMessage></aSendMessage>
                    </b-tab>
                    <b-tab title="Contact">
                        <br>
                        <aContact></aContact>
                    </b-tab>
                    <b-tab title="Guests">
                        <br>
                        <aGuests></aGuests>
                    </b-tab>
                    <b-tab title="Messages">
                        <br>
                        <aMessages></aMessages>
                    </b-tab>
                </b-tabs>
            </bCard>
            <br>
        </div>
    </div>
</template>

<script>
    import bTab from 'bootstrap-vue/es/components/tabs/tab';
    import bTabs from 'bootstrap-vue/es/components/tabs/tabs';
    import bCard from 'bootstrap-vue/es/components/card/card';
    import aCalendly from '../partials/aCalendly';
    import aSendMessage from '../partials/aSendMessage';
    import aContact from '../partials/aContact';
    import aGuests from '../partials/aGuests'
    import aMessages from '../partials/aMessages'

    export default {
        name: 'aContactMe',
        components: {
            aCalendly,
            aSendMessage,
            aContact,
            aGuests,
            aMessages,
            bTab,
            bTabs,
            bCard,
        },
        props: {
            userName: '',
            userEmail: '',
        },
    };
</script>
