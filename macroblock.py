def intra_predict(neighbors):
        # Unpack the neighbors tuple
        top_row = neighbors[0]
        left_column = neighbors[1]
 
        # Initialize empty predicted macroblocks
        dc_pred = empty((16,16))
        h_pred = empty((16,16))
        v_pred = empty((16,16))

        dc_residual = [empty((4,4))] * 16
        h_residual = [empty((4,4))] * 16
        v_residual = [empty((4,4))] * 16

        # Create the intra predictions
        for x in range(16):
            for y in range(16):
                dc_pred[y,x] = top_row[0]
                h_pred[y, x] = left_column[y]
                v_pred[y, x] = top_row[x]

        #dc_pred = empty((16,16)).fill(top_row[0])

        # Evaluate the residuals for SNR
        for x in range(4):
            for y in range(4):
                dc_residual[y*4+x]  = dc_pred[x*4:x*4+4, y*4:y*4+4] - self.blocks[y+x*4].block
                h_residual[y*4+x]   = h_pred[x*4:x*4+4, y*4:y*4+4] - self.blocks[y+x*4].block
                v_residual[y*4+x]   = v_pred[x*4:x*4+4, y*4:y*4+4] - self.blocks[y+x*4].block
        
        # Pick the smallest value (if above threshold) for the entire macroblock
        dc_snr = [(id, abs(dc_x.mean())) for id, dc_x in enumerate(dc_residual)] 
        dc_sum = sum(x[1] for x in dc_snr)
        #dc_best = min(dc_snr, key = lambda t: t[1])

        h_snr = [(id, abs(h_x.mean())) for id, h_x in enumerate(h_residual)]
        h_sum = sum(x[1] for x in h_snr)
        #h_best = min(h_snr, key = lambda t: t[1])

        v_snr = [(id, abs(v_x.mean())) for id, v_x in enumerate(v_residual)]
        v_sum = sum(x[1] for x in v_snr)
        #v_best = min(v_snr, key = lambda t: t[1])
        
        logger.info("DC SNR: %f H_SNR: %f V_SNR: %f", dc_sum, h_sum, v_sum)

        best_modes = [("dc", dc_sum), ("v", v_sum), ("h", h_sum)]
        best_mode = min(best_modes, key = lambda t: t[1])

        # Create reverse mapping from the best mode to the blocks of the best mode
        def best_blocks(x):
            return {
                'dc': dc_residual,
                'h': h_residual,
                'v' : v_residual
            }[x]

        # Set the prediction mode and insert the residual to be coded
        for x in range(4):
            for y in range(4):
                self.blocks[x*4+y].block = best_blocks(best_mode[0])[y*4+x]
                self.blocks[x*4+y].prediction_mode = best_mode[0]
                #logger.info("Picking mode %s for block %i", best_mode[x*4+y], )

        return best_mode[0]
