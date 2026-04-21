---
layout: default
title: Home - HdAugenringe 3D
---

<div class="hero">
    <div class="hero-bg"></div>
    <div class="hero-content">
        <h1>Bringing Your Ideas to Life in 3D</h1>
        <p>Your local expert for custom dragons, fidget toys, pop culture merchandise, and practical solutions.</p>
        <a href="#services" class="btn-primary" style="display:inline-block;">Explore Offerings</a>
    </div>
</div>

<div class="container" id="services">
    <h2>What I Offer</h2>
    <div class="grid">
        <div class="card">
            <h3>🐉 Dragons & Fidget Toys</h3>
            <p>Fascinating, articulated dragons and satisfying fidget toys available in a massive variety of colors. Perfect for gifts or personal collections!</p>
            <br>
            <a href="{{ '/dragons.html' | relative_url }}">View Gallery &rarr;</a>
        </div>
        <div class="card">
            <h3>⚔️ Pop Culture Merch</h3>
            <p>Exclusive 3D printed merchandise inspired by Lord of the Rings, Star Wars, Harry Potter, and more. Highly detailed and customizable.</p>
            <br>
            <a href="{{ '/merch.html' | relative_url }}">Explore Merch &rarr;</a>
        </div>
        <div class="card">
            <h3>🔧 Practical Solutions</h3>
            <p>Need a replacement part, a custom bracket, or a unique tool? I specialize in designing and printing solutions for everyday problems.</p>
            <br>
            <a href="{{ '/practical.html' | relative_url }}">See Solutions &rarr;</a>
        </div>
    </div>
</div>

<div class="container" style="margin-top: 5rem;">
    <h2>Materials, Colors & Pricing</h2>
    <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
        <div class="card">
            <h3>Vibrant Colors</h3>
            <p>I have an extensive library of premium filaments at my disposal. Whether you want sleek matte black, dual-color silk that shifts as you turn it, or glow-in-the-dark, I have exact colors to perfectly match your vision.</p>
        </div>
        <div class="card">
            <h3>Transparent Pricing</h3>
            <p>Every project is unique! Pricing is primarily based on:</p>
            <ul style="margin-top: 10px; margin-bottom: 10px;">
                <li style="margin-left: 20px;">Amount of material used</li>
                <li style="margin-left: 20px;">Total print time</li>
                <li style="margin-left: 20px;">Required custom 3D modeling (if any)</li>
            </ul>
            <p>Contact me for a free quote on any project!</p>
        </div>
    </div>
</div>

<div class="container" id="contact" style="margin-top: 5rem; margin-bottom: 5rem;">
    <h2>Get in Touch</h2>
    <p style="text-align: center; margin-bottom: 2rem; color: var(--text-secondary);">Interested in a personal recommendation or quote? Fill out the form or reach out directly!</p>
    
    <div class="contact-form">
        <!-- Form Action points to Formspree. Once you sign up for Formspree.io, put your form's ID here! -->
        <form action="https://formspree.io/f/YOUR_FORM_ID_HERE" method="POST">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" name="_replyto" required>
            </div>
            <div class="form-group">
                <label for="message">What are you looking for?</label>
                <textarea id="message" name="message" rows="5" required></textarea>
            </div>
            <button type="submit" class="btn-primary form-submit-btn">Send Message</button>
        </form>
    </div>
</div>
