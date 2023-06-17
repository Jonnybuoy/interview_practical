<template>
<div>
  <form v-on:submit.prevent="submitDepositForm">
    <label>Deposit amount:</label>
    <input type="number" id="deposit_amount" v-model="deposit_amount">
    <button class="py-4 px-6 bg-green-600 text-white rounded-lg">Submit</button>
  </form>
</div>

<div>
    <form v-on:submit.prevent="submitWithdrawalForm">
    <label>Withdraw amount:</label>
    <input type="number" id="withdrawal_amount" v-model="withdrawal_amount">
    <button class="py-4 px-6 bg-green-600 text-white rounded-lg">Submit</button>
  </form>
</div>

<div>
  <form v-on:submit.prevent="submitTransferForm">
    <label>Transfer amount:</label>
    <input type="number" id="transfer_amount" v-model="amount">
    <button class="py-4 px-6 bg-green-600 text-white rounded-lg">Submit</button>
  </form>
</div>

<div>
  <p>Available balance:</p>
</div>
</template>

<script>
import axiosClient from '../axiosClient';

export default {
  
  data() {
    return {
      deposits: [],
      withdrawal: [],
      transfers: [],
      deposit_amount: '',
      withdrawal_amount: '',
      amount: '',
    }
  },

  methods: {
    async submitDepositForm() {
      try {
        const response =  await axiosClient.post('http://127.0.0.1:8000/core/deposits/', {
          deposit_amount: this.deposit_amount,
          account: "771388e2-244d-4d31-b394-a99834494e51"
        });

        this.deposits.push(response.data);

        this.deposit_amount = ''
      } catch (error) {
        console.log(error)
      }
    },
    async submitWithdrawalForm() {
      try {
        const response =  await axiosClient.post('http://127.0.0.1:8000/core/withdrawals/', {
          withdrawal_amount: this.withdrawal_amount,
          account: "771388e2-244d-4d31-b394-a99834494e51"
        });

        this.withdrawals.push(response.data);

        this.withdrawal_amount = ''
      } catch (error) {
        console.log(error)
      }
    },
    async submitTransferForm() {
      try {
        const response =  await axiosClient.post('http://127.0.0.1:8000/core/transactions/', {
          amount: this.amount,
          sender: "771388e2-244d-4d31-b394-a99834494e51",
          receiver: "611d4f32-5fa9-47ce-83eb-61e77af18925"
        });

        this.transfers.push(response.data);

        this.amount = ''
      } catch (error) {
        console.log(error)
      }
    },

  }
}

</script>

<style>

</style>