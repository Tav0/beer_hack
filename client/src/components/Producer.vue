<template>
    <div class="producer">
        <input v-model="fridgeID" placeholder="Fridge ID">
        <button @click="addChild">Submit</button>
        <table>
            <thead>
                <tr>
                    <th>Data 6-pack</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in dataArr">
                    <td>
                        <p>{{item.uuid}}</p>
                    </td>
                    <td>
                        <p>{{item.temp}} C</p>
                        <p>{{item.humidity}}</p>
                        <p>{{time}}</p>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    import { database } from '../db'

    export default {
        name: 'producer',
        data () {
            return {
                fridgeID: '',
                dataArr: [],
                time: ''
            }
        },
        firebase: {
            items: database.ref('data')

        },
        methods: {
            addChild () {
                debugger
                const info = this.items

                for (let i in info) {
                    let itemData = info[i]

                    if (itemData['.key'] === this.fridgeID) {
                        debugger
                        this.dataArr = itemData
                        this.time = Date(itemData.time)
                    }
                }
            }
        }
    }
</script>

<style scoped>
</style>
