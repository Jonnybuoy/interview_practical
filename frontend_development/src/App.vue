<template>
<nav  class="py-10 px-8 border-b border-gray-200">
    <div class="max-w-7xl mx-auto">
        <div class="flex items-center justify-between">
            <div class="menu-left">
                <a href="#" class="text-xl text-green-700">PesPap!</a>
            </div>

            <div class="menu-center flex space-x-12">
                <a href="#" class="text-green-700">
                    <h2>My Account</h2>
                </a>

                <a href="#">
                    <h2>Login</h2>
                </a>
                
                <a href="#">
                    <h2>Sign Up</h2> 
                </a>

            </div>

        </div>
    </div>
</nav>

<main class="px-8 py-6 bg-gray-100">
    <RouterView />
</main>
    
</template>

