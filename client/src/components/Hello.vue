<template>
    <div class="main">
        <h1>{{msg}}</h1>
        <div><img class="logo" src="../assets/logo.png" /></div>
        <p>Keep your 6-packs intelligent to enjoy them more!</p>
    </div>
</template>

<script>
    export default {
        name: 'main',
        data () {
            return {
                msg: 'SMART 6-pack'
            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    h1, h2 {
        font-weight: normal;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        display: inline-block;
        margin: 0 10px;
    }

    a {
        color: #42b983;
    }
    .logo {
        width: 500px;
        height: 400px;
    }
</style>
