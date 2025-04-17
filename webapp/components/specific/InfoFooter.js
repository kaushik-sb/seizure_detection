/**
 * @class InfoFooter
 * @description Generic footer containing authorship / licence info.
 * - Made for <screen-input>. 
 * - Uses <app-root>'s features (global state, routing).
 * @extends HTMLElement
 */
class InfoFooter extends HTMLElement {

  constructor() {
    super();
  }

  connectedCallback() {
    this.renderInnerHTML();
  }

  renderInnerHTML() {
    this.innerHTML = /*html*/`
    <hr>

    <h3>Made in 2024 by</h3>

    <p>
      <a href="https://github.com/kaushik-sb" title="Kaushik on GitHub">Kaushik Subbiah</a> with the CNS Lab at IIT Madras</a>.
    </p>



    <p>
      <strong>This software was built and made available for research purposes only and is intended for use on rodent data.</strong>
    </p>
    `;

  }
  
}
customElements.define('info-footer', InfoFooter);