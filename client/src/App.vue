<template>
    <div id="app">
        <transition name="slide" mode="out-in">
            <router-view></router-view>
        </transition>
        <div>
            <router-link to="/">Home</router-link>
            <router-link to="/producer">Producer</router-link>
            <router-link to="/retailer">Retailer</router-link>
            <router-link to="/consumer">Consumer</router-link>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'app'
    }
</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }
    .slide-enter-active {
        transition: all .3s ease;
    }
    .slide-enter, .slide-leave-active {
        opacity: 0;
    }
    .slide-enter {
        transform: translateX(-3rem);
    }
    .slide-leave-active {
        transition: all .2s ease;
        transform: translateX(3rem);
    }
</style>
