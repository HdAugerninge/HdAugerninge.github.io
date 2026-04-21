---
layout: default
title: Startseite - Fantasy Printing Art
lang: de
---

<div class="hero">
    <div class="hero-bg"></div>
    <div class="hero-content">
        <h1>Ihre Ideen in 3D zum Leben erweckt</h1>
        <p>Ihr lokaler Experte für maßgeschneiderte Drachen, Fidget-Toys, Nerd-Kram und praktische Problemlösungen.</p>
        <a href="#services" class="btn-primary" style="display:inline-block;">Angebote entdecken</a>
    </div>
</div>

<div class="container" id="services">
    <h2>Was ich biete</h2>
    <div class="grid">
        <div class="card">
            <h3>🐉 Bewegliche Drachen</h3>
            <p>Faszinierende, hochdetaillierte bewegliche Drachen in einer riesigen Farbvielfalt. Perfekt als Blickfang oder durchdachtes Geschenk!</p>
            <br>
            <a href="{{ '/dragons.html' | relative_url }}">Drachen ansehen &rarr;</a>
        </div>
        <div class="card">
            <h3>🧩 Fidget Toys</h3>
            <p>Endlos zufriedenstellende, interaktive 3D-gedruckte Fidget-Toys. Ideal, um den Geist zu beruhigen und die Hände zu beschäftigen.</p>
            <br>
            <a href="{{ '/fidgets.html' | relative_url }}">Fidgets entdecken &rarr;</a>
        </div>
        <div class="card">
            <h3>⚔️ Nerd Stuff</h3>
            <p>Exklusiver 3D-gedruckter Nerd-Kram inspiriert von Herr der Ringe, Star Wars, Harry Potter und mehr. Hochdetailliert und anpassbar.</p>
            <br>
            <a href="{{ '/nerdstuff.html' | relative_url }}">Nerd-Kram ansehen &rarr;</a>
        </div>
        <div class="card">
            <h3>🔧 Praktische Lösungen</h3>
            <p>Brauchen Sie ein Ersatzteil, eine passgenaue Halterung oder ein einzigartiges Werkzeug? Ich spezialisiere mich auf das Entwerfen und Drucken von Lösungen für alltägliche Probleme.</p>
            <br>
            <a href="{{ '/practical.html' | relative_url }}">Lösungen ansehen &rarr;</a>
        </div>
    </div>
</div>

<div class="container" style="margin-top: 5rem;">
    <h2>Materialien, Farben & Preise</h2>
    <div class="grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
        <div class="card">
            <h3>Leuchtende Farben</h3>
            <p>Ich verfüge über eine umfangreiche Auswahl an Premium-Filamenten. Egal ob schickes Mattschwarz, zweifarbiges Seiden-Filament, das die Farbe im Licht wechselt, oder leuchtendes Glow-in-the-Dark – ich habe genau die richtige Farbe für Ihre Vorstellung.</p>
        </div>
        <div class="card">
            <h3>Transparente Preise</h3>
            <p>Jedes Projekt ist einzigartig! Basis der Preisgestaltung:</p>
            <ul style="margin-top: 10px; margin-bottom: 10px;">
                <li style="margin-left: 20px;">Die Menge des benötigten Materials</li>
                <li style="margin-left: 20px;">Die reine Druckzeit</li>
                <li style="margin-left: 20px;">Benötigte individuelle 3D-Modellierung</li>
            </ul>
            <p>Kontaktieren Sie mich gerne für ein kostenloses, persönliches Angebot!</p>
        </div>
    </div>
</div>

<div class="container" id="contact" style="margin-top: 5rem; margin-bottom: 5rem;">
    <h2>Kontaktieren Sie Mich</h2>
    <p style="text-align: center; margin-bottom: 2rem; color: var(--text-secondary);">An einem Projekt oder persönlichen Empfehlungen interessiert? Einfach das Formular ausfüllen oder mich direkt kontaktieren!</p>
    
    <div class="contact-form">
        <div data-fs-success style="color: var(--accent-cyan); text-align: center; margin-bottom: 1rem; font-weight: 800;">Vielen Dank für Ihre Nachricht! Ich melde mich in Kürze.</div>
        <div data-fs-error style="color: #ff6b6b; text-align: center; margin-bottom: 1rem;">Hoppla! Es gab ein Problem beim Senden.</div>
        
        <form id="my-form">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" data-fs-field required>
                <span data-fs-error="name" style="color: #ff6b6b; font-size: 0.85rem; display: block; margin-top: 5px;"></span>
            </div>
            <div class="form-group">
                <label for="email">E-Mail Adresse</label>
                <input type="email" id="email" name="email" data-fs-field required>
                <span data-fs-error="email" style="color: #ff6b6b; font-size: 0.85rem; display: block; margin-top: 5px;"></span>
            </div>
            <div class="form-group">
                <label for="message">Wie kann ich helfen?</label>
                <textarea id="message" name="message" rows="5" data-fs-field required></textarea>
                <span data-fs-error="message" style="color: #ff6b6b; font-size: 0.85rem; display: block; margin-top: 5px;"></span>
            </div>
            <button type="submit" class="btn-primary form-submit-btn" data-fs-submit-btn>Nachricht Senden</button>
        </form>
    </div>

    <!-- Formspree AJAX Script -->
    <script>
      window.formspree = window.formspree || function () { (formspree.q = formspree.q || []).push(arguments); };
      formspree('initForm', { formElement: '#my-form', formId: 'mgornylp' });
    </script>
    <script src="https://unpkg.com/@formspree/ajax@1" defer></script>
</div>
