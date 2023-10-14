import React, { FC } from "react";

const Footer: FC = () => (
  <footer className="w-full py-4 border-t border-border">
    <div className="container-fluid text-xs text-text-alts">
      <nav>
        <ul>
          <li> &copy;{new Date().getFullYear()} Argo & UTDallas</li>
        </ul>
      </nav>
    </div>
  </footer>
);

export { Footer };
