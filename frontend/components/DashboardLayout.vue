<template>
    <div class="drawer lg:drawer-open">
        <input id="dashboard-layout" type="checkbox" class="drawer-toggle" />

        <div class="drawer-content">
            <slot />
        </div> 

        <div class="drawer-side">
          <label for="dashboard-layout" aria-label="close sidebar" class="drawer-overlay"></label> 
          <ul class="menu p-4 w-80 min-h-full bg-base-200 text-base-content">
            <!-- Sidebar content here -->
            <li><a href="/dashboard">Dashboard</a></li>
            <li><a href="/scrapping">Scrapping</a></li>
            <!-- <li><a href="/history">Historique</a></li> -->
          </ul>
        </div>
      </div>
</template>