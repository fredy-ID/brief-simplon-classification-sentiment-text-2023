<template>
  <header>
      <nav>
        <div class="navbar">
          <div class="navbar-start">
            <div class="dropdown">
              <div class="block md:hidden">
                <label tabindex="0" class="btn btn-ghost btn-circle">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7" /></svg>
                </label>
                <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
                  <li><a href="/dashboard">Dashboard</a></li>
                  <li><a href="/scrapping">Lobby</a></li>
                  <li><a href="/history">Parties en ligne</a></li>
                </ul>
              </div>
            </div>
          </div>
          <div class="navbar-center">
            <a href="/" class="btn btn-ghost normal-case text-xl">Sentiment classification 🔥</a>
          </div>
          <div class="navbar-end"></div>
        </div>
      </nav>
    </header>
</template>