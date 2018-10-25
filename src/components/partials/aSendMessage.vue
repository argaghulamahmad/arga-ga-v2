<template>
  <div class="sendMessageContainer p-3 p-lg-5 d-flex flex-column my-auto">
    <h2 class="mb-5">Leave a message</h2>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group id="formInputGroup1"
                    label="Email address:"
                    label-for="formInput1"
                    description="We'll never share your email with anyone else.">
        <b-form-input id="formInput1"
                      type="email"
                      :value="this.user.userEmail"
                      required
                      placeholder="Enter email" disabled>
        </b-form-input>
      </b-form-group>
      <b-form-group id="formInputGroup2"
                    label="Your Name:"
                    label-for="formInput2">
        <b-form-input id="formInput2"
                      type="text"
                      :value="this.user.userName"
                      required
                      placeholder="Enter name" disabled>
        </b-form-input>
      </b-form-group>
      <b-form-group id="formInputGroup5"
                    label="Subject:"
                    label-for="formInput5">
        <b-form-input id="formInput5"
                      v-model="form.subject"
                      type="text"
                      required
                      placeholder="Enter message subject">
        </b-form-input>
      </b-form-group>
      <b-form-group id="formInputGroup3"
                    label="Is Important:"
                    label-for="formInput3">
        <b-form-select id="formInput3"
                       :options="level"
                       required
                       v-model="form.level">
        </b-form-select>
      </b-form-group>
      <b-form-group id="formInputGroup4"
                    label="Message:"
                    label-for="formInput4">
        <b-form-textarea id="textarea1"
                         v-model="form.message"
                         placeholder="Enter something"
                         :rows="3"
                         :max-rows="6">
        </b-form-textarea>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
      <span style="padding: 0 4px 0 4px"></span>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
    <br>
    <!--Message has been sent Modal-->
    <b-modal ref="successModal" :ok-only="true"
             id="modal-center" centered title="Message has been sent!">
      <p class="my-4">Your message has been sent!</p>
    </b-modal>
  </div>
</template>

<script>
/* eslint-disable no-underscore-dangle,no-unused-vars,no-console */

import bForm from 'bootstrap-vue/es/components/form/form';
import bFormInput from 'bootstrap-vue/es/components/form-input/form-input';
import bFormGroup from 'bootstrap-vue/es/components/form-group/form-group';
import bFormSelect from 'bootstrap-vue/es/components/form-select/form-select';
import bFormCheckboxGroup from 'bootstrap-vue/es/components/form-checkbox/form-checkbox-group';
import bFormCheckbox from 'bootstrap-vue/es/components/form-checkbox/form-checkbox';
import bFormTextarea from 'bootstrap-vue/es/components/form-textarea/form-textarea';
import bButton from 'bootstrap-vue/es/components/button/button';
import bModal from 'bootstrap-vue/es/components/modal/modal';
import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
  name: 'aSendMessage',
  components: {
    bForm,
    bFormInput,
    bFormGroup,
    bFormSelect,
    bFormCheckboxGroup,
    bFormCheckbox,
    bButton,
    bFormTextarea,
    bModal,
  },
  data() {
    return {
      user: {
        userName: '',
        userEmail: '',
      },
      form: {
        subject: '',
        message: '',
        level: null,
      },
      level: [
        { text: 'Select One', value: null },
        'Critical',
        'Important',
        'Normal',
        'Unimportant',
      ],
      show: true,
    };
  },
  methods: {
    ...mapGetters(['getUserName', 'getUserEmail', 'getUserPhotoUrl']),
    onReset(evt) {
      evt.preventDefault();
      /* Reset our form values */
      this.form.level = null;
      this.form.message = '';
      /* Trick to reset/clear native browser form validation state */
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
    showModal() {
      this.$refs.successModal.show();
    },
    hideModal() {
      this.$refs.successModal.hide();
    },
    onSubmit(evt) {
      evt.preventDefault();
      const _this = this;

      let Message = class {
          constructor(sender_name, sender_email, subject, body, level) {
            this.sender_name = sender_name;
            this.sender_email = sender_email;
            this.subject = subject;
            this.body = body;
            this.level = level;
          }
        };

      let message = new Message(this.user.userName, this.user.userEmail, this.form.subject, this.form.level, this.form.message);

      axios
        .post('/api/messages/', message)
        .then((response) => {
          _this.showModal();
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  created() {
    this.user.userName = this.getUserName();
    this.user.userEmail = this.getUserEmail();
  },
};
</script>
